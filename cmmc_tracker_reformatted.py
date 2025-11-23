import json
import os
import csv
from datetime import datetime
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter


class Control:
    """Represents a single NIST 800-171 control with compliance tracking capabilities.

    Each control has static properties (Id, family, control text, CMMC level, SPRS points)
    imported from the NIST requirements file, and dynamic properties (status, implementation
    date, evidence, notes) that track the organization's compliance progress.
    """

    def __init__(self, control_id, family, control_text, cmmc_level, sprs_points,
                 status="Not Started", implementation_date=None, evidence=None, notes=""):
        """Initialize a Control object with security control details.

        Args:
            control_id (str): Unique identifier for the control (e.g., '3.1.1')
            family (str): Control family name (e.g., 'Access Control', 'Audit and Accountability')
            control_text (str): Full text description of the control requirement
            cmmc_level (int): CMMC level (1 or 2) that this control belongs to
            sprs_points (int): Point value for SPRS scoring (deducted if not implemented)
            status (str): Current implementation status ('Not Started', 'In Progress', 
                         'Implemented', or 'Verified'). Defaults to 'Not Started'
            implementation_date (str): ISO date (YYYY-MM-DD) when control was first implemented. 
                                      Defaults to None
            evidence (list): List of evidence dictionaries containing 'description' and 
                           'date_added' keys. Defaults to None (converted to empty list)
            notes (str): Additional notes about the control implementation. Defaults to empty string
        """
        self.id = control_id
        self.family = family
        self.control = control_text
        self.cmmc_level = cmmc_level
        self.sprs_points = sprs_points
        self.status = status
        self.implementation_date = implementation_date
        # Avoid mutable default argument bug: check for None and create new list
        # Using [] as default would cause all Control instances to share the same list object
        self.evidence = evidence if evidence is not None else []
        self.notes = notes

    def to_dict(self):
        """Convert control object to dictionary for JSON serialization.

        Returns:
            dict: Dictionary containing all control attributes with keys matching
                  the JSON file format for data persistence
        """
        return {
            "Id": self.id,
            "family": self.family,
            "control": self.control,
            "cmmc_level": self.cmmc_level,
            "SPRS points": self.sprs_points,
            "status": self.status,
            "implementation_date": self.implementation_date,
            "evidence": self.evidence,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Control instance from a dictionary (class method constructor).

        This method is used to reconstruct Control objects when loading data from JSON files.
        It's a class method that acts as an alternative constructor.

        Args:
            data (dict): Dictionary containing control data loaded from JSON file with keys:
                        'Id', 'family', 'control', 'cmmc_level', 'SPRS points',
                        'status', 'implementation_date', 'evidence', 'notes'

        Returns:
            Control: New Control object initialized with data from the dictionary
        """
        return cls(
            control_id=data["Id"],
            family=data["family"],
            control_text=data["control"],
            cmmc_level=data["cmmc_level"],
            sprs_points=data["SPRS points"],
            # Use .get() with defaults for optional fields that may not exist in older saved data
            status=data.get("status", "Not Started"),
            implementation_date=data.get("implementation_date"),
            evidence=data.get("evidence", []),
            notes=data.get("notes", "")
        )


class ComplianceTracker:
    """Track NIST 800-171 and CMMC compliance status across all security controls.

    This class manages the complete lifecycle of compliance tracking including:
    - Loading control definitions from CSV/Excel files
    - Tracking implementation status for each of the 110 NIST 800-171 controls
    - Calculating SPRS scores (range: -203 to 110)
    - Monitoring progress toward CMMC Level 1 and Level 2 certification
    - Managing evidence documentation
    - Generating comprehensive Excel compliance reports
    - Persisting all data to JSON files for session continuity

    Attributes:
        filename (str): Path to JSON file for data persistence
        csv_filename (str): Path to CSV/Excel file with control definitions
        sheet_name (str): Name of Excel sheet to read (if applicable)
        data (dict): Main data structure containing organization info and all controls
    """

    def __init__(self, filename="compliance_data.json", csv_filename="sp800-171r2-security-reqs.csv", sheet_name="SP 800-171 Requirements"):
        """Initialize the ComplianceTracker with file paths and load existing data.

        Args:
            filename (str): Name of JSON file for storing compliance data. Defaults to 'compliance_data.json'
            csv_filename (str): Name of CSV/Excel file containing NIST control definitions. Defaults to 'sp800-171r2-security-reqs.csv'
            sheet_name (str): Name of Excel sheet to read from (if using Excel file). Defaults to 'SP 800-171 Requirements'

        Note:
            All files are expected to be in the same directory as the script.
            If JSON file doesn't exist, creates new data structure from CSV/Excel file.
        """
        # Get the directory where this script is located (not current working directory)
        # This ensures files are saved/loaded from script location regardless of where script is run from
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Build full absolute paths for all files
        self.filename = os.path.join(script_dir, filename)
        self.csv_filename = os.path.join(script_dir, csv_filename)
        self.sheet_name = sheet_name
        # Load existing data from JSON or initialize new data structure from CSV/Excel
        self.data = self.load_data()

    def load_data(self):
        """Load compliance data from JSON file and convert to Control objects.

        Returns:
            dict: Dictionary containing organization info, last_updated timestamp,
                  and list of Control objects. If file doesn't exist or is corrupted,
                  returns newly initialized data structure.

        Note:
            Automatically handles JSON decode errors and missing files by initializing
            fresh data from the CSV/Excel control definitions file.
        """
        # Check if the JSON data file already exists
        if os.path.exists(self.filename):
            try:
                # Attempt to load and parse the JSON file
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    # Convert control dictionaries back to Control objects using list comprehension
                    # This reconstructs the object instances from the serialized data
                    data["controls"] = [Control.from_dict(
                        ctrl) for ctrl in data["controls"]]
                    return data
            except json.JSONDecodeError:
                # File exists but is corrupted/invalid - start fresh
                print("Error reading file. Starting with empty data.")
                return self.initialize_data()
        else:
            # File doesn't exist - create new data structure from CSV/Excel
            return self.initialize_data()

    def save_data(self):
        """Save compliance data to JSON file with proper data integrity measures.

        Note:
            - Converts Control objects to dictionaries before JSON serialization
            - Uses flush() and fsync() to ensure data is written to disk immediately
            - Prints confirmation message with file path after successful save
        """
        # Convert Control objects to dictionaries for JSON serialization
        # Must do this because JSON can't directly serialize Python objects
        data_to_save = {
            "organization": self.data["organization"],
            "last_updated": self.data["last_updated"],
            # Use list comprehension to convert all Control objects to dictionaries
            "controls": [ctrl.to_dict() for ctrl in self.data["controls"]]
        }
        # Write the data to file with proper formatting
        with open(self.filename, 'w') as f:
            # indent=4 makes the JSON human-readable with nice formatting
            json.dump(data_to_save, f, indent=4)
            # Force write to disk immediately (don't just buffer in memory)
            f.flush()  # Flush Python's internal buffer to OS
            os.fsync(f.fileno())  # Force OS to write to physical disk
        print(f"Data saved to {self.filename}")

    def load_controls_from_csv(self):
        """Load controls from CSV or Excel file with automatic format detection.

        Supports both CSV and Excel (.xlsx, .xls) file formats. Automatically detects
        the file type based on extension and uses appropriate parsing method.

        Expected column mapping (zero-indexed):
            Column A (0): Family - Control family name
            Column C (2): Id - Control identifier (e.g., '3.1.1')
            Column E (4): Control - Full control description text
            Column G (6): CMMC_Level - CMMC level number (1 or 2)
            Column H (7): SPRS_Points - Point value for SPRS scoring

        Returns:
            list: List of Control objects parsed from the file. Returns empty list
                  if file not found or if parsing errors occur.

        Note:
            - Skips header row automatically
            - Skips rows with missing critical data (id, family, or control text)
            - Prints warnings for rows that can't be parsed
            - For Excel files, can specify sheet name via self.sheet_name
        """
        # Initialize empty list to store parsed Control objects
        controls = []

        # Validate that the control definitions file exists
        if not os.path.exists(self.csv_filename):
            print(f"Warning: File '{self.csv_filename}' not found.")
            print("Please ensure the file exists in the same directory as this script.")
            return controls

        # Check file extension to determine if it's Excel or CSV
        # splitext returns (name, extension), we take [1] for extension and lowercase it
        file_ext = os.path.splitext(self.csv_filename)[1].lower()

        try:
            if file_ext in ['.xlsx', '.xls']:
                # Handle Excel file using openpyxl library
                # data_only=True gets calculated cell values instead of formulas
                workbook = load_workbook(self.csv_filename, data_only=True)

                # Determine which sheet to read from
                if self.sheet_name:
                    # Check if the requested sheet name exists in the workbook
                    if self.sheet_name in workbook.sheetnames:
                        sheet = workbook[self.sheet_name]
                        print(f"Reading from sheet: '{self.sheet_name}'")
                    else:
                        # Sheet not found - provide helpful error and use first sheet
                        print(f"Warning: Sheet '{self.sheet_name}' not found.")
                        print(f"Available sheets: {workbook.sheetnames}")
                        print(f"Using first sheet: '{workbook.sheetnames[0]}'")
                        sheet = workbook.active
                else:
                    # No sheet specified - use first sheet by default
                    sheet = workbook.active
                    print(f"No sheet specified. Using: '{sheet.title}'")
                    print(f"Available sheets: {workbook.sheetnames}")

                # Read rows from Excel sheet, starting at row 2 to skip header row
                # values_only=True returns cell values instead of cell objects (more efficient)
                rows = list(sheet.iter_rows(min_row=2, values_only=True))

            else:
                # Handle CSV file using standard library csv module
                with open(self.csv_filename, 'r', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    # Skip header row (first row contains column names)
                    next(reader, None)
                    # Convert remaining rows to list for processing
                    rows = list(reader)

            # Process each row and create Control objects
            # Start enumeration at 2 to match Excel row numbers (1=header, data starts at 2)
            for row_num, row in enumerate(rows, start=2):
                try:
                    # Check if row has enough columns (need at least 8 columns: A through H)
                    if not row or len(row) < 8:
                        continue

                    # Extract data from specific columns (0-indexed)
                    # Column mapping: A=0 (Family), C=2 (Id), E=4 (Control),
                    #                 G=6 (CMMC_Level), H=7 (SPRS_Points)
                    # Use .strip() to remove leading/trailing whitespace from all fields
                    family = str(row[0]).strip() if row[0] else ""
                    control_id = str(row[2]).strip() if row[2] else ""
                    control_text = str(row[4]).strip() if row[4] else ""
                    cmmc_level = str(row[6]).strip() if row[6] else ""
                    sprs_points = str(row[7]).strip() if row[7] else ""

                    # Skip rows with missing critical data (ID, family, or control text required)
                    if not control_id or not family or not control_text:
                        continue

                    # Create Control object with parsed data
                    # Convert CMMC level and SPRS points from strings to integers
                    # Use float() first in case Excel stored as decimal, then int() to convert
                    # Default to level 2 and 0 points if conversion fails or value is empty
                    control = Control(
                        control_id=control_id,
                        family=family,
                        control_text=control_text,
                        cmmc_level=int(float(cmmc_level)) if cmmc_level else 2,
                        sprs_points=int(float(sprs_points)
                                        ) if sprs_points else 0
                    )
                    controls.append(control)
                except (ValueError, IndexError) as e:
                    # If we encounter a data conversion error, skip this row with a warning
                    print(f"Warning: Skipping row {row_num} due to error: {e}")
                    continue

            # Print summary of how many controls were successfully loaded
            print(f"Successfully loaded {len(controls)} controls from file")

        except Exception as e:
            # Catch any file reading errors and return empty list
            print(f"Error reading file: {e}")
            return controls

        return controls

    def initialize_data(self):
        """Create initial data structure with all NIST 800-171 controls from CSV/Excel file.

        Loads the complete set of 110 NIST 800-171 controls from the configured CSV or
        Excel file and creates a new compliance tracking data structure.

        Returns:
            dict: Dictionary containing:
                - organization (str): Organization name
                - last_updated (str): ISO timestamp of last update
                - controls (list): List of Control objects with default 'Not Started' status

        Note:
            If no controls can be loaded from file, creates structure with empty control list
            and prints a warning message.
        """
        # Load all 110 controls from the CSV/Excel file
        controls = self.load_controls_from_csv()

        # Warn if no controls were loaded (file might be missing or malformed)
        if not controls:
            print(
                "Warning: No controls loaded from CSV. Starting with empty control list.")

        # Create and return the initial data structure
        return {
            # Default organization name (can be changed by user)
            "organization": "Cognos",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Current timestamp
            "controls": controls  # List of all Control objects, all starting at "Not Started" status
        }

    def update_status(self, req_id, status, notes=""):
        """Update the compliance status of a control and save changes.

        Args:
            req_id (str): Control identifier (e.g., '3.1.1')
            status (str): New status - must be one of: 'Not Started', 'In Progress',
                         'Implemented', or 'Verified'
            notes (str): Optional notes about the status change. Defaults to empty string

        Behavior:
            - Validates status against allowed values
            - Sets implementation_date automatically when status changes to 'Implemented'
              or 'Verified' (only if date not already set)
            - Updates last_updated timestamp
            - Saves data to JSON file automatically
            - Prints confirmation or error message

        Note:
            Implementation date is only set on first transition to 'Implemented' or 'Verified'
            to preserve the original compliance date even if status changes later.
        """
        # Define list of valid status values for validation
        valid_statuses = ["Not Started",
                          "In Progress", "Implemented", "Verified"]

        # Validate that the provided status is one of the allowed values
        if status not in valid_statuses:
            print(f"Invalid status. Choose from:" + {valid_statuses})
            return

        # Find the control with the matching ID
        for ctrl in self.data["controls"]:
            if ctrl.id == req_id:
                # Update the control's status and notes
                ctrl.status = status
                ctrl.notes = notes
                # Only set implementation date on first transition to Implemented/Verified
                # This preserves the original compliance date even if status changes later
                # Check if status is compliant AND date hasn't been set yet
                if status in ["Implemented", "Verified"] and ctrl.implementation_date is None:
                    ctrl.implementation_date = datetime.now().strftime("%Y-%m-%d")
                # Update the last_updated timestamp for the entire dataset
                self.data["last_updated"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S")
                # Save changes to JSON file immediately
                self.save_data()
                print(f"Updated {req_id} to {status}")
                return

        # If we got here, the control ID wasn't found in the list
        print(f"Control {req_id} not found")

    def add_evidence(self, req_id, evidence_description):
        """Add evidence documentation for a specific control.

        Args:
            req_id (str): Control identifier (e.g., '3.1.1')
            evidence_description (str): Description of the evidence being documented

        Behavior:
            - Creates evidence entry with description and current date
            - Appends evidence to control's evidence list
            - Updates last_updated timestamp
            - Saves changes to JSON file automatically
            - Prints confirmation or error message

        Note:
            Evidence is stored as a dictionary with 'description' and 'date_added' keys.
            Multiple evidence entries can be added to the same control.
        """

        # Find the control with the matching ID
        for ctrl in self.data["controls"]:
            if ctrl.id == req_id:
                # Store evidence as dictionary with description and ISO date
                # This allows multiple evidence entries per control with timestamps
                ctrl.evidence.append({
                    "description": evidence_description,
                    "date_added": datetime.now().strftime("%Y-%m-%d")
                })
                # Update the last_updated timestamp for the entire dataset
                self.data["last_updated"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S")
                # Save changes to JSON file immediately
                self.save_data()
                print(f"Added evidence to {req_id}")
                return

        # If we got here, the control ID wasn't found in the list
        print(f"Control {req_id} not found")

    def get_SPRS_score(self):
        """Calculate and display the current SPRS (Supplier Performance Risk System) score.

        SPRS scoring methodology:
            - Perfect score: 110 points (all controls implemented)
            - Points are deducted for each control not in 'Implemented' or 'Verified' status
            - Deduction amount equals the control's sprs_points value
            - Minimum possible score: -203 (all controls 'Not Started')

        Behavior:
            Calculates score and prints formatted result to console.
            Does not return a value - output is displayed directly.

        Note:
            Only controls with status 'Implemented' or 'Verified' contribute to the score.
            Controls with status 'Not Started' or 'In Progress' result in point deductions.
        """
        # Start with perfect SPRS score
        beginning_points = 110
        lost_points = 0
        # Loop through all controls and deduct points for non-compliant ones
        for ctrl in self.data["controls"]:
            # Only Not Started and In Progress controls lose points
            if ctrl.status in ["Not Started", "In Progress"]:
                lost_points += ctrl.sprs_points
            else:
                # Implemented or Verified status results in no points lost
                pass
        # Calculate final score by subtracting lost points from perfect score
        total_points = beginning_points - lost_points
        print("\n=== SPRS Score ===")
        print(f"Current SPRS Score: {total_points}")

    def get_cmmc_level_status(self, level):
        """Check and display completion status for a specific CMMC level.

        Args:
            level (int): CMMC level to check (1 or 2)

        CMMC Level Behavior:
            CMMC levels are additive:
            - Level 1: Includes only level 1 controls
            - Level 2: Includes both level 1 AND level 2 controls

        Display:
            - Shows count of implemented vs total controls for the level
            - If incomplete, lists all remaining control IDs that need implementation
            - Prints error message if no controls found for specified level

        Note:
            A control is considered complete only if status is 'Implemented' or 'Verified'.
        """
        # Include all controls up to the specified level because CMMC is additive
        # Level 2 includes both Level 1 and Level 2 controls
        # Use list comprehension to filter controls where cmmc_level <= requested level
        level_reqs = [ctrl for ctrl in self.data["controls"]
                      if ctrl.cmmc_level <= level]

        # Error handling if the incorrect level is provided, or no controls for the level exist
        if not level_reqs:
            print(f"No controls found for CMMC Level {level}")
            return

        # Count controls that are implemented or verified using generator expression
        # sum() with generator is memory-efficient for counting
        implemented = sum(1 for ctrl in level_reqs if ctrl.status in [
                          "Implemented", "Verified"])
        total = len(level_reqs)

        print(f"\nCMMC Level {level} Progress:")
        print(f"  {implemented} of {total} controls implemented")

        if implemented < total:
            print(f"  Remaining controls:")
            for ctrl in level_reqs:
                if ctrl.status not in ["Implemented", "Verified"]:
                    print(f"    - {ctrl.id}")

    def get_family_summary(self):
        """Generate and display compliance summary organized by control family.

        Behavior:
            - Groups all controls by their family (e.g., 'Access Control', 'Audit and Accountability')
            - Counts total controls and implemented controls for each family
            - Displays results in alphabetical order by family name
            - Shows 'X of Y controls implemented' for each family

        Display Format:
            === Summary by Control Family ===
            [Family Name] has [implemented] of [total] controls implemented

        Note:
            A control is considered implemented if status is 'Implemented' or 'Verified'.
            All 14 NIST 800-171 control families are included if they have controls.
        """
        # Dictionary to store counts by family: {family_name: {total: n, implemented: m}}
        families = {}

        # Loop through all controls and aggregate by family
        for ctrl in self.data["controls"]:
            family = ctrl.family
            # Initialize family entry if not seen before
            if family not in families:
                families[family] = {"total": 0, "implemented": 0}

            # Increment total count for this family
            families[family]["total"] += 1
            # Increment implemented count only if control is complete
            if ctrl.status in ["Implemented", "Verified"]:
                families[family]["implemented"] += 1

        # Display results
        print("\n=== Summary by Control Family ===")
        # Sort families alphabetically for consistent output
        for family in sorted(families.keys()):
            total = families[family]["total"]
            implemented = families[family]["implemented"]
            print(f"{family} has {implemented} of {total} controls implemented")

    def export_to_excel(self, filename=None):
        """Export comprehensive compliance data to formatted Excel workbook.

        Args:
            filename (str): Path for output Excel file. If None, uses default name
                           'compliance_report.xlsx' in same directory as JSON file.

        Creates two worksheets:
            1. Summary Sheet:
               - Organization info and last update timestamp
               - Current SPRS score
               - Overall status distribution (counts by status)
               - Compliance breakdown by control family

            2. Controls Details Sheet:
               - Complete list of all 110 controls with:
                 * ID, Family, CMMC Level, Control description
                 * Status, Implementation date
                 * Evidence (with dates)
                 * Notes

        Formatting:
            - Professional styling with header colors and fonts
            - Optimized column widths for readability
            - Text wrapping for long content (evidence, notes, control text)

        Returns:
            str: Path to created Excel file, or None if save failed (e.g., file is open)

        Error Handling:
            Catches PermissionError if file is open and displays helpful message.
        """
        if filename is None:
            # Use the same directory as the JSON file for the Excel report
            # Default filename: compliance_report.xlsx
            filename = os.path.join(os.path.dirname(
                self.filename), "compliance_report.xlsx")

        # Create new Excel workbook
        wb = Workbook()

        # === Summary Sheet ===
        # The active sheet becomes the Summary sheet
        ws_summary = wb.active
        ws_summary.title = "Summary"

        # === Define header styling ===
        # Blue background with white text for professional appearance
        header_fill = PatternFill(
            start_color="366092", end_color="366092", fill_type="solid")
        header_font = Font(color="FFFFFF", bold=True)

        # === Summary information ===
        # Add title and metadata
        ws_summary['A1'] = "NIST 800-171 / CMMC Compliance Report"
        ws_summary['A1'].font = Font(size=14, bold=True)
        ws_summary['A2'] = f"Organization: {self.data['organization']}"
        ws_summary['A3'] = f"Last Updated: {self.data['last_updated']}"

        # Calculate SPRS score for display in summary (same logic as get_SPRS_score method)
        beginning_points = 110
        lost_points = 0
        for ctrl in self.data["controls"]:
            if ctrl.status in ["Not Started", "In Progress"]:
                lost_points += ctrl.sprs_points
        sprs_score = beginning_points - lost_points

        ws_summary['A4'] = f"Current SPRS Score: {sprs_score}"
        ws_summary['A4'].font = Font(size=12)

        # === Overall statistics section ===
        ws_summary['A6'] = "Overall Compliance Status"
        ws_summary['A6'].font = Font(size=14, bold=True)

        total = len(self.data["controls"])
        # Count how many controls are in each status using dictionary
        statuses = {}
        for ctrl in self.data["controls"]:
            status = ctrl.status
            # Increment count for this status (default to 0 if not seen yet)
            statuses[status] = statuses.get(status, 0) + 1

        # Create status table with headers
        row = 7
        ws_summary['A7'] = "Status"
        ws_summary['B7'] = "Count"
        # Apply header formatting to both cells in the status table header
        for cell in ['A7', 'B7',]:
            ws_summary[cell].fill = header_fill
            ws_summary[cell].font = header_font

        # Fill in status counts
        row = 8
        for status in ["Not Started", "In Progress", "Implemented", "Verified"]:
            count = statuses.get(status, 0)
            ws_summary[f'A{row}'] = status
            ws_summary[f'B{row}'] = count
            row += 1

        # === Family summary section ===
        row += 1  # Add one blank row after status table
        ws_summary[f'A{row}'] = "Compliance by Control Family"
        ws_summary[f'A{row}'].font = Font(size=14, bold=True)

        families = {}
        for ctrl in self.data["controls"]:
            family = ctrl.family
            if family not in families:
                families[family] = {"total": 0, "implemented": 0}
            families[family]["total"] += 1
            if ctrl.status in ["Implemented", "Verified"]:
                families[family]["implemented"] += 1

        row += 1
        ws_summary[f'A{row}'] = "Control Family"
        ws_summary[f'B{row}'] = "Implemented"
        ws_summary[f'C{row}'] = "Total"
        for cell in [f'A{row}', f'B{row}', f'C{row}']:
            ws_summary[cell].fill = header_fill
            ws_summary[cell].font = header_font

        row += 1
        for family in sorted(families.keys()):
            total_fam = families[family]["total"]
            implemented = families[family]["implemented"]
            ws_summary[f'A{row}'] = family
            ws_summary[f'B{row}'] = implemented
            ws_summary[f'C{row}'] = total_fam
            row += 1

        # Adjust column widths for optimal readability
        ws_summary.column_dimensions['A'].width = 47
        ws_summary.column_dimensions['B'].width = 12.5
        ws_summary.column_dimensions['C'].width = 12.5

        # === Detailed controls Sheet ===
        # Create second worksheet for detailed control information
        ws_details = wb.create_sheet("Controls Details")

        # Define column headers for details sheet
        headers = ["ID", "Family", "CMMC Level", "Control",
                   "Status", "Implementation Date", "Evidence", "Notes"]
        # Write headers with formatting
        for col, header in enumerate(headers, 1):
            cell = ws_details.cell(row=1, column=col)
            cell.value = header
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(wrap_text=True)

        # Add all controls to the details sheet
        # Start at row 2 (row 1 is headers), enumerate gives us idx starting at 2
        for idx, ctrl in enumerate(self.data["controls"], 2):
            # Write basic control information
            ws_details.cell(row=idx, column=1, value=ctrl.id)
            ws_details.cell(row=idx, column=2, value=ctrl.family)
            ws_details.cell(row=idx, column=3, value=ctrl.cmmc_level)
            ws_details.cell(row=idx, column=4, value=ctrl.control)
            ws_details.cell(row=idx, column=5, value=ctrl.status)
            # Use empty string instead of None for cells without implementation date
            ws_details.cell(row=idx, column=6,
                            value=ctrl.implementation_date or "")

            # Format evidence as multi-line string with dates
            # Each evidence entry shows as "[date] description"
            evidence_text = ""
            if ctrl.evidence:
                evidence_list = []
                for ev in ctrl.evidence:
                    evidence_list.append(
                        f"[{ev['date_added']}] {ev['description']}")
                # Join all evidence entries with newlines for multi-line display
                evidence_text = "\n".join(evidence_list)
            ws_details.cell(row=idx, column=7, value=evidence_text)
            # Enable text wrapping for evidence cell to display multi-line content properly
            ws_details.cell(row=idx, column=7).alignment = Alignment(
                wrap_text=True)

            # Add notes with text wrapping
            ws_details.cell(row=idx, column=8, value=ctrl.notes)
            # Enable text wrapping for notes cell
            ws_details.cell(row=idx, column=8).alignment = Alignment(
                wrap_text=True)

        # Adjust column widths for details sheet to optimal sizes for readability
        # Widths determined by typical content length and Excel character units
        ws_details.column_dimensions['A'].width = 6.34
        ws_details.column_dimensions['B'].width = 35.22
        ws_details.column_dimensions['C'].width = 11
        ws_details.column_dimensions['D'].width = 227.5
        ws_details.column_dimensions['E'].width = 10.11
        ws_details.column_dimensions['F'].width = 14.67
        ws_details.column_dimensions['G'].width = 50
        ws_details.column_dimensions['H'].width = 30

        # === Save the workbook ===
        try:
            wb.save(filename)
            print(f"\nExcel report exported to: {filename}")
            return filename
        except PermissionError:
            # File is probably open in Excel - provide helpful error message
            print(f"\n*** ERROR: Cannot save the Excel file ***")
            print(f"The file is currently open in another program.")
            print(
                f"Please close '{os.path.basename(filename)}' and try again.")
            return None


def main():
    """Main program loop providing interactive menu for NIST 800-171/CMMC compliance tracking.

    Menu Options:
        1. Check CMMC Level Status - View progress toward CMMC Level 1 or 2 certification
        2. Get SPRS Score - Calculate current SPRS score (range: -203 to 110)
        3. View Summary by Family - See implementation progress by control family
        4. Add Evidence - Document evidence for a specific control
        5. Update Control Status - Change implementation status of a control
        6. Export to Excel - Generate comprehensive Excel compliance report
        7. Save and Exit - Save all changes and close program

    Features:
        - Input validation for all user entries
        - Case-insensitive status input (converts to title case)
        - Control ID validation against loaded controls
        - Error handling for invalid choices and data entry
        - Option to update status immediately after adding evidence

    Note:
        - All changes are auto-saved to JSON file after each operation
        - Data persists between sessions
        - Sheet name can be customized by modifying tracker initialization
    """
    # Initialize the ComplianceTracker
    # Specify the sheet name here if your file has multiple sheets
    # Example: tracker = ComplianceTracker(sheet_name="Security Requirements")
    tracker = ComplianceTracker()

    # Main program loop - continues until user selects option 7 (Save and Exit)
    while True:
        # Display menu
        print("\n=== NIST 800-171 / CMMC Compliance Tracker ===")
        print("1. Check CMMC Level Status")
        print("2. Get SPRS Score")
        print("3. View Summary by Family")
        print("4. Add Evidence")
        print("5. Update Control Status")
        print("6. Export to Excel")
        print("7. Save and Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            # Option 1: Check CMMC Level Status
            # Error handling for entering wrong CMMC level or non-integer input
            try:
                level = int(input("Enter CMMC level (1-2): "))
                # Validate level is either 1 or 2
                if level not in [1, 2]:
                    print("Error: CMMC level must be 1 or 2")
                    continue
                tracker.get_cmmc_level_status(level)
            except ValueError:
                # User entered something that's not a number
                print("Error: Please enter a valid number (1 or 2)")

        elif choice == "2":
            # Option 2: Get SPRS Score
            tracker.get_SPRS_score()

        elif choice == "3":
            # Option 3: View Summary by Family
            tracker.get_family_summary()

        elif choice == "4":
            # Option 4: Add Evidence
            req_id = input("Enter control ID (e.g., 3.1.1): ").strip()
            # Validate control ID is not empty
            if not req_id:
                print("Error: Control ID cannot be empty")
                continue
            # Validate control ID exists by searching through all loaded controls
            control_exists = False
            for ctrl in tracker.data["controls"]:
                if req_id == ctrl.id:
                    control_exists = True
                    break
            # If control not found, display error and restart loop
            if not control_exists:
                print("Error: Invalid control ID. Control does not exist.")
                print("Please enter a valid control ID (e.g., 3.1.1, 3.14.7)")
                continue
            # Get evidence description and validate it's not empty
            evidence = input("Enter evidence description: ").strip()
            if not evidence:
                print("Error: Evidence description cannot be empty")
                continue
            # Add the evidence to the control
            tracker.add_evidence(req_id, evidence)

            # Ask if user wants to update status for the same control (convenience feature)
            # This avoids needing to select menu option 5 separately
            update_status = input(
                "\nWould you like to update the status for this control? (yes/no): ").strip().lower()
            if update_status in ['yes', 'y']:
                valid_statuses = ["Not Started",
                                  "In Progress", "Implemented", "Verified"]
                # Loop until user provides valid status
                while True:
                    print(
                        "\nStatus options: Not Started, In Progress, Implemented, Verified")
                    # .title() converts input to Title Case for case-insensitive matching
                    status = input("Enter new status: ").strip().title()
                    if status in valid_statuses:
                        notes = input("Enter notes (optional): ").strip()
                        tracker.update_status(req_id, status, notes)
                        break
                    else:
                        print(
                            f"Error: Invalid status. Must be one of: {', '.join(valid_statuses)}")
                        print("Please try again.")

        elif choice == "5":
            # Option 5: Update Control Status
            req_id = input("Enter control ID (e.g., 3.1.1): ").strip()
            # Validate control ID is not empty
            if not req_id:
                print("Error: Control ID cannot be empty")
                continue
            # Validate control ID exists by searching through all loaded controls
            control_exists = False
            for ctrl in tracker.data["controls"]:
                if req_id == ctrl.id:
                    control_exists = True
                    break
            if not control_exists:
                print("Error: Invalid control ID. Control does not exist.")
                print("Please enter a valid control ID (e.g., 3.1.1, 3.14.7)")
                continue

            valid_statuses = ["Not Started",
                              "In Progress", "Implemented", "Verified"]
            # Loop until user provides valid status
            while True:
                print(
                    "\nStatus options: Not Started, In Progress, Implemented, Verified")
                # .title() converts input to Title Case for case-insensitive matching
                status = input("Enter new status: ").strip().title()
                if status in valid_statuses:
                    notes = input("Enter notes (optional): ").strip()
                    tracker.update_status(req_id, status, notes)
                    break
                else:
                    # Invalid status - show error and loop again
                    print(
                        f"Error: Invalid status. Must be one of: {', '.join(valid_statuses)}")
                    print("Please try again.")

        elif choice == "6":
            # Option 6: Export to Excel
            try:
                tracker.export_to_excel()
            except Exception as e:
                # Catch any unexpected errors during Excel generation
                print(f"Error exporting to Excel: {e}")
                print("Please ensure the file is not open and try again.")

        elif choice == "7":
            # Option 7: Save and Exit
            # Save data one final time before exiting (though auto-saved after each change)
            tracker.save_data()
            print("Good luck on your compliance journey!")
            break  # Exit the while loop and end program

        else:
            # Invalid menu choice - prompt user to try again
            print("Invalid choice. Please try again.")


# Standard Python idiom: only run main() if script is executed directly
# (not imported as a module)
if __name__ == "__main__":
    main()

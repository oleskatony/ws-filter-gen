# Wireshark Filter Generator

This is a simple GUI application built using Python's `tkinter` library that helps generate Wireshark SIP filters based on `Call-ID` or `Contact URI`. You can either include or exclude the specified items from the filter and the generated filter will be copied to your clipboard for easy use in Wireshark.

## Features

- **Call-ID Filter**: Generate a filter that matches or excludes specified `Call-ID`s.
- **Contact URI Filter**: Generate a filter that matches or excludes specified `Contact URI`s.
- **Exclude Option**: Option to either include or exclude the specified data in the filter.
- **Clipboard Copy**: The generated filter is automatically copied to your clipboard.

## Usage

1. Paste the list of `Call-ID`s or `Contact URI`s into the provided text area (one per line).
2. Select the filter type from the dropdown (`Call-ID Filter` or `Contact URI Filter`).
3. Check the "Exclude these items" option if you want to exclude the items from the filter.
4. Click the "Generate Filter" button. The filter will be copied to your clipboard and a success message will be displayed.

## Dependencies

- Python 3.x
- `tkinter` (included with standard Python distributions)

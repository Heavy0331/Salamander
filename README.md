# Salamander

Salamander is a program designed to help you create and manage minutes of a meeting. It provides a graphical user interface built using `customtkinter`, allowing you to add, edit, and organize meeting events. The program also supports publishing the minutes to a webhook when you're done.


## Table of Contents
| Section                       | Description                                    |
|-------------------------------|------------------------------------------------|
| [Features](#features)         | A list of all the benefits of using Salamander |
| [Requirements](#requirements) | The list of required modules to run Salamander |
| [Installation](#installation) | How to install Salamander                      |
| [Usage](#usage)               | How to run Salamander                          |
| [Debugging](#debugging)       | How to enable and use debugging mode           |
| [Testing](#testing)           | Information on testing Salamander              |
| [Support](#support)           | How to get support for Salamander              |
| [License](#license)           | The license utilized                           |
| [Contributing](#contributing) | How to contribute to the development           |


## Features

- Add and edit meeting events with information like name, description, time, and type.
- Organize and display events in a user-friendly interface.
- Publish the minutes to a webhook for easy sharing.

## Requirements

- Python 3.x
- `customtkinter` package

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Heavy0331/Salamander.git
   cd Salamander
   
2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt

## Usage

Run the program:

    python main.py

    
   The program's GUI window will open. You can perform the following actions:
   
   ![image](https://github.com/Heavy0331/Salamander/assets/111214932/55eff0ee-af6b-4280-b416-a850ca744b53)
   - Add a new event: Click the "New Event" button, fill in the event details, and click "Add Event."
   ![image](https://github.com/Heavy0331/Salamander/assets/111214932/5302c469-c88b-4f89-83f7-67e13f99a391)

   ![image](https://github.com/Heavy0331/Salamander/assets/111214932/f5a08609-6a27-441c-be66-b55f2282eec8)
   - Edit an event: Click an existing event button to edit its details.
     
   ![image](https://github.com/Heavy0331/Salamander/assets/111214932/54e96a93-6180-45c0-83f2-d9e194da39d7)
   - Publish minutes: Click the "Publish" button to send the minutes to a webhook. (Discord only)
     
   ![image](https://github.com/Heavy0331/Salamander/assets/111214932/1c48686a-eecb-481a-8684-e76b2fc4453d)

[Link back up](#table-of-contents)

## Debugging
Salamander includes a built-in debugging mode, which can only be enabled by editing the source code. To enable debugging mode, open `main.py` and change the value of `allow_debug` to `True`. This will enable the following features:
- 5 events will be made, in numerical order upon clicking "Debug."
- The console will print the contents of the minutes file upon clicking "Debug."

You can activate debugging mode by pressing ctrl+d, assuming it is enabled.

**Note**: Debugging mode is ***NOT*** enabled by default, and you should never
edit the source code unless you know what you're doing. Any edits to the
source code are your responsibility to maintain unless you create a pull
request that is approved. This option should only be utilized by developers,
and is not intended for end-users. Please submit a bug report if you find
any issues with the program.

[Link back up](#table-of-contents)


## Testing
Testing is always appreciated! If you would like to test the program,
even if you don't plan on using Salamander. You may submit any feedback
or bug reports to the GitHub issue tracker, or follow the instructions
in the [Support](#support) section to contact the developer directly.
You can also edit the source code and make actual changes to the
program by following the instructions in the [Contributing](#contributing)
section.

[Link back up](#table-of-contents)


## Support
All support is provided through the GitHub issue tracker. If you have any
questions, feature requests, or bug reports, please open a new issue
[here](https://github.com/Heavy0331/Salamander/issues), after checking
to make sure that your issue has not already been reported. Duplicates
will be closed and labeled as such.

For immediate support, you can DM @krakendev on Discord,
but please note that this is not the preferred method of
support, and if your issue is not immediate, you may be
asked to open a GitHub issue instead, blocked, or
ignored.

**Note**: Please do not contact Heavy0331 for support. He is not
a current maintainer of the project, and will not be able to
provide any assistance, and this will likely lead to
1) Your issue being ignored
2) Delaying of your issue being resolved
3) Future issues being ignored or closed

[Link back up](#table-of-contents)
        

## License
This project uses the BSD 3-Clause License.
See [LICENSE](https://github.com/Heavy0331/Salamander/blob/main/LICENSE)
for more information.


## Contributing

Contributions are welcome! If you have suggestions,
improvements, or bug fixes, feel free to submit a pull request.

[Link back up](#table-of-contents)

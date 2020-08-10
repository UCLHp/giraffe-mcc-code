# giraffe-mcc-code
Conversion from PTW's water tank mcc format to Giraffe's csv format.

## Description
A calibration measurement is needed each time the Giraffe is used.
The calibration measurement needs a corresponding water phantom reference measurement in RFB/csv format.
Our reference measurement comes from the PTW water tank which outputs mcc files.

## Use
Specify the name of your mcc file in the MCC_FILENAME variable and run the code: ```python mcc_to_csv.py```

## License
```
Copyright (C) 2020 Anamaria Barburas

Conversion of  PTW wanter tank's mcc files to Giraffe's csv format.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
from __future__ import print_function
from Scoreboard import ScoreBoard
from Results import Results
from FileReader import argumentReader
from Storage import Register
import traceback
import sys

argumentReader.parse_files(sys.argv[1], sys.argv[2], sys.argv[3])


sc = ScoreBoard()
Results.print_header()
try:
    sc.execute()
    results = sc.get_result()
except Exception as e:
    print(traceback.format_exc(), file=sys.stdout)


# for result in results:
#     result.print_row()

print("Result is done")

Register.print_values()

from __future__ import print_function
from Scoreboard import ScoreBoard
from Results import Results
import FileReader
from Storage import Register
import traceback
import sys

sc = ScoreBoard()
Results.print_header()
try:
    sc.execute()
    results = sc.get_result()
except Exception as e:
    # print("Exception: {0}".format(e.))
    print(traceback.format_exc(), file=sys.stdout)


# for result in results:
#     result.print_row()

print("Result is done")

#Register.print_values()

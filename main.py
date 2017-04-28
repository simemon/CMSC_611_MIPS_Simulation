from __future__ import  print_function
from Scoreboard import  ScoreBoard
from Results import  Results
import FileReader

sc = ScoreBoard()
sc.execute()
results = sc.get_result()

Results.print_header()

for result in results:
    result.print_row()

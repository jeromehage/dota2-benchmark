# dota2-benchmark

1. Download PresentMon-1.9.0-x64.exe, put it in the project folder.

https://github.com/GameTechDev/PresentMon

2. Run 'run.bat' as admin, it will do the following:

```
PresentMon-1.9.0-x64.exe -process_name dota2.exe -hotkey "f11" -delay 1 -timed 80
```

This makes F11 collect frame time data for Dota 2 for 80 seconds, after a delay of 1 second

3. Start Dota 2 and type these in console:

```
fps_max 0
enginenofucus 0
```

4. Watch match ID: 7233123840 (Liquid vs Quest)

5. In console, type:

```
demo_goto 71000 pause
```

6. Close console, then press F9 (unpause) and then F11, and wait 81 seconds

7. Collect a few samples (3+) for each hardware configuration

8. You will have a .csv for each test, group them in folders

9. Run parse.py to get the summary file results.csv

10. Run graphs.py to get the horizontal bar plot
# dota2-benchmark

Note: You can skip steps 1 and 2 and use software like CapFrameX.

How to:
1. Download PresentMon-2.1.0-x64.exe, put it in the project folder.
    https://github.com/GameTechDev/PresentMon/releases

2. Run run.bat as admin, it will do the following:

    ```
    PresentMon-2.1.0-x64.exe -process_name dota2.exe -hotkey "f11" -delay 1 -timed 120
    ```

    This makes F11 collect frame time data for Dota 2 for 2 minutes, after a delay of 1 second.

3. Start Dota 2, and add a hotkey for the console by going to:

    - Settings: top left
    - Hotkeys: top left
    - Advanced: bottom center
    - Console: top right
	
    The default hotkey is backslash \

4. Open the console and type these commands:

    ```
    fps_max 0
    ```

    ```
    engine_no_focus_sleep 0
    ```

5. Back in the main screen, from the top, click on Watch > Replays > and type the match ID in the top right box:

    7839880889 (Quest vs Liquid)

6. Download and watch the replay (bottom right blue button).

7. Select English broadcast.

8. Open the console and type:

    ```
    demo_goto 58500 pause
    ```

    The ingame time will be 14:45.


    Note: due to a recent replay bug, use this without pausing.

    ```
    demo_goto 58500
    ```

9.  Press F9 and F11, to unpause and record (and wait 121 seconds).

9. Collect a few samples (3+) for each hardware configuration (.csv files).

10. Group the files by hardware configuration in subfolders.

    Ex: folders named 'DDR4-3200', 'DDR4-3600'

11. Run parse.py to get the summary results.csv file.

12. Run graphs.py to get the horizontal bar plot.

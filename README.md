# How to use this
1. If you haven't already, `cd` into the repository.
2. Create a virtual environment, activate it, and execute `pip install -r requirements.txt`.
3. Back out of the virtual environment and execute `npm install`[^1].
4. Now that setup is finished, you will want to download data for your respective leaderboard. I've made `fetch-stats.js` to help you retrieve this, as well as `download.sh` which will download it for you. Because of the monkeytype API ratelimits, this will take a while to download.
    1. `./download.sh <mode> <mode2> [starting-page]`
    2. Example use: `./download.sh time 60`, `./download.sh time 15 4`
5. Then, you will want to run `generate.sh` which uses `generate.py`. Now is a good time to mention that the shellscripts provided are written to use command line arguments to make my life easier, so you may find that you have to modify the scripts and possibly even their corresponding python files.
6. View the HTML files with the plotted data.

[^1]: As of this commit, there are currently no dependencies, so this step may not be strictly necessary.
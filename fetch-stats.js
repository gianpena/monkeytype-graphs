const fs = require('fs');
const args = process.argv.slice(2);

async function writeStatsToFile(stats) {
    
    const filePath = `./${args[0]}${args[1]}.json`;
    try {
        const fileContent = fs.existsSync(filePath) ? fs.readFileSync(filePath, 'utf8') : '[]';
        const existingStats = [...JSON.parse(fileContent), ...stats ];
        fs.writeFileSync(filePath, JSON.stringify(existingStats, null, 2));
    } catch (err) {
        console.error(`Error reading or writing ${filePath}:`, err);
    }

}

let page = args[2] ? parseInt(args[2]) : 0;

async function fetchStats() {

    let isPageComplete = true;
    let lastPage = page + 500;
    for(; isPageComplete && page < lastPage; ++page) {
        const requestStr = `https://api.monkeytype.com/leaderboards?language=english&mode=${args[0]}&mode2=${args[1]}&page=${page}&pageSize=200`;
        const response = await fetch(requestStr);
        if(response.status === 429) {
            console.log(`Ratelimited on ${requestStr}.`);
            return false;
        }
        const { data } = await response.json();
        if(!data) {
            console.log(`Request successful but no data found:\n${requestStr}`);
            return false;
        }
        const { entries } = data;
        await writeStatsToFile(entries);
        
        isPageComplete = entries && entries.length === 200;

    }

    return isPageComplete;

}

const callback = async () => {
    const isComplete = await fetchStats();
    if(isComplete) process.exit(0);
};
callback();
setInterval(callback, 1 * 60 * 60 * 1000 + 10000);
// feelings/apology_handler.js

const fs = require('fs');

// Simulating apology success based on silent treatment config
function attemptApology() {
    let success = Math.random() > 0.4; // 60% chance
    if (fs.existsSync('../bugs/silent_treatment.config')) {
        console.log("😶 Silent Treatment Active. Apology difficulty increased!");
        success = Math.random() > 0.8; // Only 20% chance
    }
    if (success) {
        console.log("🙏 Apology Accepted!");
    } else {
        console.log("🚪 Apology Ignored. Slammed Door Noise.");
    }
}

module.exports = { attemptApology };

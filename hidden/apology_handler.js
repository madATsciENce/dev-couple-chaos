// apology_handler.js

class ApologyHandler {
    constructor(partner) {
        this.partner = partner;
        this.errorLog = [];
    }

    apologize(issue) {
        console.log(`[Apology] Sorry for ${issue}, dear ${this.partner} 😔.`);
        this.errorLog.push(issue);
    }

    generateExcuses() {
        return [
            "It was network lag 😭",
            "I misinterpreted the API call!",
            "Temporary emotional downtime 🧠",
        ];
    }

    escalateToFlowers() {
        console.log("Deploying flower bouquet 🚀💐...");
    }
}

const apologySystem = new ApologyHandler("You ❤️");

apologySystem.apologize("forgetting important date");
apologySystem.escalateToFlowers();

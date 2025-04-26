class ApologyHandler {
    constructor() {
      this.errors = [
        "Didn’t notice haircut 💇‍♀️",
        "Forgot good morning text ☀️",
        "Watched Netflix series without you 📺",
      ];
    }
  
    generateApology(error) {
      console.log(`I'm really sorry for: ${error}`);
      console.log("Please accept these flowers 🌸 + endless hugs 🤗.");
    }
  
    run() {
      this.errors.forEach(error => {
        this.generateApology(error);
      });
    }
  }
  
  const apology = new ApologyHandler();
  apology.run();
  
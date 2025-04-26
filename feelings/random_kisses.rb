class RandomKisses
    def initialize
      @kisses = ["Forehead Kiss 💋", "Cheek Kiss 😚", "Hand Kiss 🤝", "Nose Kiss 🐽"]
    end
  
    def deliver
      loop do
        puts "Sending a #{@kisses.sample} to you! 💖"
        sleep(rand(2..5))
      end
    end
  end
  
  kisser = RandomKisses.new
  kisser.deliver
  
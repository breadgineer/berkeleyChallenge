public class Pokemon {
    public String name;
    public int level;
    public static String trainer = "Ash";
    public static int partySize = 0;
    public Pokemon(String name, int level) {
        this.name = name;
        this.level = level;
        this.partySize += 1;
    }

    public static void main(String[] args) {
          Pokemon p = new Pokemon("Pikachu", 17);
          Pokemon j = new Pokemon("Jolteon", 99);
          System.out.println("Party size: " + Pokemon.partySize); //2
          p.printStats(); // Pikachu 17 Ash
          int level = 18;
          Pokemon.change(p, level);
          p.printStats(); // Pikachu 18 Team Rocket
          Pokemon.trainer = "Ash";
          j.trainer = "Brock";
          p.printStats(); // Pikachu 18 Brock
          /*
          * if we were to call Pokemon.printStats() here we will get an error because
          * we cannot call an instance method from a static object
          * after excecution we get 'non-static method printStats() cannot be referenced from a static context'
          * */
//          Pokemon.printStats();
      }

      public static void change(Pokemon poke, int level) {
          poke.level = level;
          /*
          * Here level is a local variable created inside the
          * scope of the change method
          *  */
          level = 50;
          poke = new Pokemon("Voltorb", 1);
          poke.trainer = "Team Rocket";
        }

      public void printStats() {
          System.out.println(name + " " + level + " " + trainer);
          }

      }
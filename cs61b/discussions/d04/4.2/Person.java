  class Person {
      void speakTo(Person other) { System.out.println("kudos"); }
      void watch(SoccerPlayer other) { System.out.println("wow"); }
  }
class Athlete extends Person {
      void speakTo(Athlete other) { System.out.println("take notes"); }
      void watch(Athlete other) { System.out.println("game on"); }
  }
class SoccerPlayer extends Athlete {
      void speakTo(Athlete other) { System.out.println("respect"); }
      void speakTo(Person other) { System.out.println("hmph"); }
  }

  /**
  Person itai = new Person();
   ..
  SoccerPlayer shivani = new Person();
   CE
  Athlete sohum = new SoccerPlayer();
   ..
  Person jack = new Athlete();
   ..
  Athlete anjali = new Athlete();
   ..
   SoccerPlayer chirasree = new SoccerPlayer();
   ..
   itai.watch(chirasree);
    wow
   jack.watch(sohum);
    game on
   itai.speakTo(sohum);
    kudos
   jack.speakTo(anjali);
  game on

   anjali.speakTo(chirasree);
 take notes
   sohum.speakTo(itai);

   chirasree.speakTo((SoccerPlayer) sohum);

   sohum.watch(itai);

   sohum.watch((Athlete) itai);

   ((Athlete) jack).speakTo(anjali);

   ((SoccerPlayer) jack).speakTo(chirasree);

   ((Person) chirasree).speakTo(itai);


   */
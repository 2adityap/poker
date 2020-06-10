
function callShuffle1(cards) {
    var i;
    for(i = 0; i < 100; i++) {
      let a = Math.floor(Math.random()*52)
      let b = Math.floor(Math.random()*52)
      shuffle1(cards,a,b)
    }
}
//Random shuffle method, just takes 2 random numbers and swaps them, works pretty well
function shuffle1(cards,i,j) {
    let temp = cards[i]
    cards[i] = cards[j];
    cards[j] = temp;
}



const cards = ["1 Spades", "2 spades", "3 spades", "4 spades", "5 spades", "6 spades","7 spades", "8 spades","9 spades","10 spades",
"Jack Spades", "Queen Spades", "Kings Spades", "1 Clubs", "2 Clubs", "3 Clubs", "4 Clubs", "5 Clubs", "6 Clubs","7 Clubs", "8 Clubs","9 Clubs","10 Clubs",
"Jack Clubs", "Queen Clubs", "Kings Clubs", "1 Diamonds", "2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds","7 Diamonds", "8 Diamonds","9 Diamonds","10 Diamonds",
"Jack Diamonds", "Queen Diamonds", "Kings Diamonds", "1 Heart", "2 Heart", "3 Heart", "4 Heart", "5 Heart", "6 Heart","7 Heart", "8 Heart","9 Heart","10 Heart",
"Jack Heart", "Queen Heart", "Kings Heart"];

callShuffle1(cards)
console.log(cards)

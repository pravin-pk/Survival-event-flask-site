document.addEventListener('contextmenu', event => event.preventDefault(alert("Right Click Disabled! Please Do not Try to Cheat"))); // Disabling Right click
const cards = document.querySelectorAll('.memory-card');
const modal = document.getElementById("modal")
let correctCount = 0;
maxCount = 1;

let hasFlippedCard = false;
let lockBoard = false;
let firstCard, secondCard;

function flipCard() {
  if (lockBoard) return;
  if (this === firstCard) return;

  this.classList.add('flip');

  if (!hasFlippedCard) {
    hasFlippedCard = true;
    firstCard = this;

    return;
  }

  secondCard = this;
  checkForMatch();
}

function checkForMatch() {
  let isMatch = firstCard.dataset.framework === secondCard.dataset.framework;

  isMatch ? disableCards() : unflipCards();
}

function disableCards() {
  firstCard.removeEventListener('click', flipCard);
  secondCard.removeEventListener('click', flipCard);
  correctCount += 1;
  resetBoard();
}

function unflipCards() {
  lockBoard = true;

  setTimeout(() => {
    firstCard.classList.remove('flip');
    secondCard.classList.remove('flip');

    resetBoard();
  }, 1100);
}

function resetBoard() {
  [hasFlippedCard, lockBoard] = [false, false];
  [firstCard, secondCard] = [null, null];
  if(correctCount == maxCount){
    // alert("Game over")
    modal.style.opacity = 1;
    modal.style.transform = "all 300ms ease-in-out";
    // setTimeout(() => {
    //   window.location.href = "/challenge2"
    // }, 5000)
  }
  // console.log(correctCount)
}

(function shuffle() {
  cards.forEach(card => {
    let randomPos = Math.floor(Math.random() * 20);
    card.style.order = randomPos;
  });
})();

cards.forEach(card => card.addEventListener('click', flipCard));
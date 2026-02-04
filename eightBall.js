// Eight Ball game
// User greeting
const userName = 'Matt';
userName ? console.log(`Hello ${userName}!`):console.log('Hello!');

// User question
const userQuestion = 'Will the sun rise tomorrow?';
if (userName) {
  console.log(`${userName} asks "${userQuestion}"`);
} else {
  console.log(userQuestion)
}
// Eight Ball answers
const randomNumber = Math.floor(Math.random() * 8);

const eightBallAnswers = [
  'It is certain',
  'It is decidedly so',
  'Reply hazy try again',
  'Cannot predict now',
  'Do not count on it',
  'My sources say no',
  'Outlook not so good',
  'Signs point to yes'
];

// Print answer
const eightBall = eightBallAnswers[randomNumber];
console.log(eightBall);
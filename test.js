// As a child runs up the stairs, they can hop up 1, 2, or 3 steps at a time. Write a function that counts the number of possible ways a child can run up a staircase with N steps.
// For example:
// Given a staircase with 4 steps, the child can run up the staircase in following 7 ways (combination of steps)
// 1,1,1,1
// 1,1,2
// 1,3
// 3,1
// 2,1,1
// 2,2 and
// 1,2,1
// So countWays(4) = 7

// n = 1 countWays(1) = 1
// n = 2 countWays(2) = 2
// n = 3 countWays(3) = 4 // 12,21,3,111

const countWays = (n) => {
  let fib1 = 1;
  let fib2 = 2;
  let fib3 = 4;
  let res = 0;

  for (i = 4; i <= n; i++) {
    res = fib1 + fib2 + fib3;
    fib1 = fib2;
    fib2 = fib3;
    fib3 = res;
  }

  return res;
};

//[1, 2, 4, 7, 14...]
// Implement 3 aspect of an automated check authoring solution:
// The conversion of a number into a text representation of the number for the check (bounded to 99,999.00)
// The appropriate markup for a semantic and accessible check
// The styles to style the check to look like the picture (basically a chance to discuss layout issues).
// https://imgur.com/EyEQkWC

const dictionary = {
  0: "zero",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
};

//num: 135.35

// "one hundred thirty five 35/100"

const converToText = (num) => {
  const decimal = (num * 100) % 100; //35
  const integer = num - decimal; //135
  let res = "";

  if (integer < 20) {
    res += dictionary[integer];
  } else if (integer < 100) {
    const tenth = Math.floor(integer / 10) * 10;
    const ones = integer % 10;
    res += dictionary[tenth];
    res += dictionary[ones];
  } else if (integer < 1000) {
    const hundred = Math.floor(integer / 100);
    res += dictionary[hundred] + "hundred";
    const tenth = Math.floor(integer / 10) * 10;
    const ones = integer % 10;
    res += dictionary[tenth];
    res += dictionary[ones];
  } else if (integer < 100000) {
    const thousand = Math.floor(integer / 1000);
    res += dictionary[thousand] + "thousand";
    const hundred = Math.floor(integer / 100);
    res += dictionary[hundred] + "hundred";
    const tenth = Math.floor(integer / 10) * 10;
    const ones = integer % 10;
    res += dictionary[tenth];
    res += dictionary[ones];
  }

  if (decimal) {
    res += `${decimal}/100`;
  }
  return res;
};

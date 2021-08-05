// const x = 10;
const x = [1, 2, 3, 4];
// const x = { member: "foo" };

const modify = (input) => {
  //   input = 50;
  input.push(5);
  //   input.member = "bar";
};

modify(x);
console.log(x);

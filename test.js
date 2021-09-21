// Given
const endorsements = [
  { skill: "css", user: "Bill" },
  { skill: "javascript", user: "Chad" },
  { skill: "javascript", user: "Bill" },
  { skill: "css", user: "Sue" },
  { skill: "javascript", user: "Sue" },
  { skill: "html", user: "Sue" },
];

const skills = [];

const aggregateSkills = (endorsements) => {
  const obj = {};

  for (const endorsement of endorsements) {
    if (!obj[endorsement.skill]) {
      obj[endorsement.skill] = {
        skill: endorsement.skill,
        users: [endorsement.user],
        count: 1,
      };
    } else {
      obj[endorsement.skill].users.push(endorsement.user);
      obj[endorsement.skill].count += 1;
    }
  }

  for (const val of Object.values(obj)) {
    skills.push(val);
  }

  skills.sort((a, b) => b.count - a.count);
};

aggregateSkills(endorsements);
// Result
console.log(skills);
// [
//   { skill: 'javascript', users: ['Chad', 'Bill', 'Sue'], count: 3 },
//   { skill: 'css', users: ['Bill', 'Sue'], count: 2 },
//   { skill: 'html', users: ['Sue'], count: 1 },
// ]

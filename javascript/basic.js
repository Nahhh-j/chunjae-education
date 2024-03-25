const person = {
  name: "Alex",
  age: 28,
};

console.log(person.name); // 사용 가능, "Alex"
console.log(person.gender); // 사용 가능, undefined

console.log(person.name.someKey); // 사용 가능, undefined
console.log(person.gender.someKey); // 사용 불가능, 에러 발생
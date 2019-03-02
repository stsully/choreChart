function todaysChores() {
  var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var d = new Date();
  alert("hello! today is " + daysOfWeek[d.getDay()]);
}

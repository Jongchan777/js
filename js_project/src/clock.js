const clockTitle = document.querySelector(".js-clock");

function getClock() {
  const date = new Date();
  const years = String(date.getFullYear());
  const months = String(date.getMonth());
  const days = String(date.getDay());
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");
  clockTitle.innerText = `${years}/${months}/${days}, ${hours}:${minutes}:${seconds}`;
}

getClock();
setInterval(getClock, 1000);

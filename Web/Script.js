function startApp() {
  document.getElementById("home").classList.add("hidden");
  document.getElementById("preferences").classList.remove("hidden");
}

function goPremium() {
  alert("Version Premium : calendrier de l’Avent, bilan annuel, mises à jour IA !");
}

function generateSuggestions() {
  const age = document.getElementById("age").value;
  const relation = document.getElementById("relation").value;
  const budget = document.getElementById("budget").value;
  const culture = document.getElementById("culture").value;

  const gifts = [
    `📦 Livre personnalisé – 25€`,
    `🎧 Casque audio – 45€`,
    `🕯️ Coffret bien-être – 30€`
  ];

  document.getElementById("preferences").classList.add("hidden");
  document.getElementById("suggestions").classList.remove("hidden");

  const list = document.getElementById("giftList");
  list.innerHTML = "";
  gifts.forEach(gift => {
    const li = document.createElement("li");
    li.textContent = gift;
    list.appendChild(li);
  });
}

function addToCalendar() {
  document.getElementById("suggestions").classList.add("hidden");
  document.getElementById("calendar").classList.remove("hidden");
}

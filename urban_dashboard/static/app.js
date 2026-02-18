const map = L.map('map').setView([10.0159, 76.3419], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'OpenStreetMap',
}).addTo(map);

let layers = [];

// page navigation
function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}

// fetch status
async function fetchStatus() {
  const res = await fetch('/alert');
  const data = await res.json();

  document.getElementById('status').textContent = JSON.stringify(data, null, 2);

  drawZones(data);
}

// draw hazard zones
function drawZones(data) {
  layers.forEach(l => map.removeLayer(l));
  layers = [];

  if (!data.zones) return;

  data.zones.forEach(zone => {
    let color = 'green';

    if (zone.type === 'flood') color = 'blue';
    if (zone.type === 'traffic') color = 'red';
    if (zone.type === 'crowd') color = 'orange';
    if (zone.type === 'power') color = 'yellow';

    const circle = L.circle([zone.lat, zone.lon], {
      radius: 1000,
      color: color,
      fillOpacity: 0.5,
    }).addTo(map);

    circle.bindPopup(`${zone.type.toUpperCase()} : ${zone.level}`);
    layers.push(circle);
  });
}

// CHAT
async function sendMessage() {
  const input = document.getElementById('chatinput');
  const msg = input.value;

  const res = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: msg }),
  });

  const data = await res.json();

  const box = document.getElementById('chatbox');
  box.innerHTML += `<div><b>You:</b> ${msg}</div>`;
  box.innerHTML += `<div><b>AI:</b> ${data.reply}</div>`;

  input.value = '';
}

setInterval(fetchStatus, 8000);
fetchStatus();

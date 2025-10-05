function calculateBudget() {
  const days = document.getElementById("days").value;
  const budget = document.getElementById("budget").value;
  const dailyBudget = budget / days;
  document.getElementById("result").innerText = `You can spend $${dailyBudget} per day on your vacation!`;
}
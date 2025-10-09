export const API_URL = "http://127.0.0.1:5000";
import { API_URL } from "./api/config";

async function analyzeUserBehavior(data) {
  const res = await fetch(`${API_URL}/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  const result = await res.json();
  console.log(result);
}

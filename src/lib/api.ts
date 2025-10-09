// Lightweight API helper for calling the Flask backend
const DEFAULT_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000';

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';

async function request<T = any>(path: string, method: HttpMethod = 'GET', body?: any) {
  const url = `${DEFAULT_BASE}${path}`;

  const opts: RequestInit = {
    method,
    headers: {
      'Content-Type': 'application/json',
    },
  };

  if (body !== undefined) opts.body = JSON.stringify(body);

  const res = await fetch(url, opts);
  const text = await res.text();

  try {
    return JSON.parse(text) as T;
  } catch (e) {
    // not JSON — return raw text
    return (text as unknown) as T;
  }
}

export async function health() {
  return request<{message: string}>('/');
}

export async function analyzeMouse(payload: Record<string, any>) {
  return request('/api/mouse', 'POST', payload);
}

export async function analyzeKeyboard(payload: Record<string, any>) {
  return request('/api/keyboard', 'POST', payload);
}

export async function analyzeFingerprint(payload: Record<string, any>) {
  return request('/api/fingerprint', 'POST', payload);
}

export default { health, analyzeMouse, analyzeKeyboard, analyzeFingerprint };

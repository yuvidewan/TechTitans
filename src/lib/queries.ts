import { useMutation, useQuery } from '@tanstack/react-query';
import api from './api';

export function useHealthQuery() {
  return useQuery({ queryKey: ['health'], queryFn: api.health, staleTime: 1000 * 60 });
}

export function useUploadMutation() {
  return useMutation({
    mutationFn: async (formData: FormData) => {
      const base = import.meta.env.VITE_API_BASE || 'http://localhost:5000';
      const res = await fetch(base + '/api/upload', { method: 'POST', body: formData });
      const json = await res.json();
      if (!res.ok) throw new Error(json?.error || 'Upload failed');
      return json;
    },
  });
}

export function useAnalyzeMouseMutation() {
  return useMutation({ mutationFn: (payload: Record<string, any>) => api.analyzeMouse(payload) });
}

export default { useHealthQuery, useUploadMutation, useAnalyzeMouseMutation };

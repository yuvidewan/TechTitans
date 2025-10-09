import { useState } from 'react';
import { Button } from '@/components/ui/button';
import api from '@/lib/api';

const BackendTest = () => {
  const [health, setHealth] = useState<string | null>(null);
  const [mouseResult, setMouseResult] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const checkHealth = async () => {
    setLoading(true);
    try {
      const res = await api.health();
      setHealth(JSON.stringify(res));
    } catch (e: any) {
      setHealth(String(e?.message || e));
    } finally {
      setLoading(false);
    }
  };

  const callMouse = async () => {
    setLoading(true);
    try {
      // sample payload - replace with real features as needed
      const sample = { x: 0.1, y: 0.2, dx: 1.0, dy: 0.5 };
      const res = await api.analyzeMouse(sample);
      setMouseResult(JSON.stringify(res));
    } catch (e: any) {
      setMouseResult(String(e?.message || e));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-8 p-6 rounded-xl bg-card/60 border-border shadow-glass max-w-xl mx-auto">
      <h4 className="text-lg font-semibold mb-3">Backend integration test</h4>
      <div className="flex gap-3">
        <Button onClick={checkHealth} disabled={loading}>Check Health</Button>
        <Button onClick={callMouse} variant="outline" disabled={loading}>Call Mouse API</Button>
      </div>

      <div className="mt-4 space-y-2">
        <div>
          <div className="text-sm text-muted-foreground">Health</div>
          <pre className="text-xs p-2 bg-muted rounded">{health ?? '—'}</pre>
        </div>

        <div>
          <div className="text-sm text-muted-foreground">Mouse result</div>
          <pre className="text-xs p-2 bg-muted rounded">{mouseResult ?? '—'}</pre>
        </div>
      </div>
    </div>
  );
};

export default BackendTest;

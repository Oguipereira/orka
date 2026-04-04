export interface User {
  id: string;
  name: string;
  email: string;
}

export interface Integration {
  id: string;
  platform: string;
  status: "connected" | "error" | "pending";
  last_sync?: string;
}

export interface Decision {
  id: string;
  type: string;
  priority: "baixa" | "media" | "alta";
  title: string;
  description: string;
  recommended_action: string;
  confidence_score: number;
  status: "pendente" | "aprovado" | "executado" | "ignorado";
  created_at: string;
}

export interface Notification {
  id: string;
  type: "alerta" | "oportunidade" | "acao";
  title: string;
  message: string;
  is_read: boolean;
  created_at: string;
}

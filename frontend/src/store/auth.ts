"use client";
import { create } from "zustand";
import { persist } from "zustand/middleware";
import api from "@/lib/api";

interface User {
  id: string;
  name: string;
  email: string;
  organization_id: string;
  role: string;
}

interface AuthState {
  user: User | null;
  loading: boolean;
  connectedPlatforms: string[];
  fetchMe: () => Promise<void>;
  addPlatform: (p: string) => void;
  logout: () => void;
}

export const useAuth = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      loading: true,
      connectedPlatforms: [],
      fetchMe: async () => {
        try {
          const { data } = await api.get("/auth/me");
          set({ user: data, loading: false });
        } catch {
          set({ user: null, loading: false });
        }
      },
      addPlatform: (p) => set((s) => ({ connectedPlatforms: [...new Set([...s.connectedPlatforms, p])] })),
      logout: () => {
        if (typeof window !== "undefined") localStorage.removeItem("orka_token");
        set({ user: null, connectedPlatforms: [] });
        window.location.href = "/login";
      },
    }),
    { name: "orka-auth", partialize: (s) => ({ connectedPlatforms: s.connectedPlatforms }) }
  )
);

import type { Metadata } from "next";
import { Inter, Space_Grotesk } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const spaceGrotesk = Space_Grotesk({ subsets: ["latin"], variable: "--font-display", weight: ["400","500","600","700"] });

export const metadata: Metadata = {
  title: "Orka — AI Intelligence Platform",
  description: "Conecte seus marketplaces. A IA analisa tudo e entrega decisões prontas.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR" className={`${inter.variable} ${spaceGrotesk.variable} h-full`}>
      <body className="h-full">{children}</body>
    </html>
  );
}

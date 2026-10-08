import "../globals.css";

export const metadata = {
  title: "Login to Hayday Store",
  description: "Create your first store in Telegram in just a few minutes"
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>{children}</body>
    </html>
  );
}

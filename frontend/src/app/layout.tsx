import "./globals.css";

export const metadata = {
  title:
    "AI Code Review Dashboard",
  description:
    "Review analytics dashboard"
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        className="bg-gray-50"
      >
        {children}
      </body>
    </html>
  );
}
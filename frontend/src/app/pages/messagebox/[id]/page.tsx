"use client";
import DashboardLayoutBasic from "@/app/components/DashboardLayoutBasic";
import Navbar from "@/app/components/Navbar";

interface PageProps {
  params: { id: number | string };
}
function MessageboxPage({ params }: PageProps) {
  return (
    <>
      <div className="flex">
        <Navbar />
        <DashboardLayoutBasic />
        <main className="flex-1 p-8 bg-gray-50 mt-14 min-h-screen">
          <h1 className="text-3xl font-bold mb-4">Welcome, Jane!</h1>
          <p>This is your dashboard content.{params.id}</p>
        </main>
      </div>
    </>
  );
}

export default MessageboxPage;

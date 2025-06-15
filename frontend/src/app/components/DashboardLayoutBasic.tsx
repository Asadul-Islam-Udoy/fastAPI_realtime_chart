import Link from "next/link";
import React, { useEffect, useState } from "react";

interface User {
  name: string;
  email: string;
  avatarUrl?: string;
}

const DashboardLayoutBasic: React.FC = () => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  useEffect(() => {
    setTimeout(() => {
      setUser({
        name: "Jane Doe",
        email: "jane.doe@example.com",
        avatarUrl: "https://i.pravatar.cc/150?img=47",
      });
      setLoading(false);
    }, 2000);
  }, []);

  return (
    <aside className="w-64 min-w-[16rem] h-screen mt-16 flex-shrink-0 border-r border-gray-200 bg-white overflow-hidden">
      {/* Search */}
      <div className="p-4 border-b border-gray-100">
        <input
          type="text"
          placeholder="Search..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div className="h-full flex flex-col overflow-y-auto">
        {/* User Info */}

        <div className="flex cursor-pointer hover:bg-blue-50 items-center  border-gray-200">
          <Link className="flex cursor-pointer hover:bg-blue-50 items-center space-x-4 p-3 border-b border-gray-200" href="/pages/messagebox/2">
            {loading ? (
              <div className="w-14 h-14 rounded-full bg-gray-300 animate-pulse" />
            ) : (
              <img
                src={user?.avatarUrl}
                alt="User avatar"
                className="w-14 h-14 rounded-full object-cover"
              />
            )}
            <div className="flex flex-col space-y-2">
              {loading ? (
                <>
                  <div className="h-4 w-32 bg-gray-300 rounded animate-pulse" />
                  <div className="h-3 w-40 bg-gray-200 rounded animate-pulse" />
                </>
              ) : (
                <>
                  <h2 className="text-lg font-semibold text-gray-900">
                    {user?.name}
                  </h2>
                  <p className="text-sm text-gray-500">{user?.email}</p>
                </>
              )}
            </div>
          </Link>
        </div>
      </div>
    </aside>
  );
};

export default DashboardLayoutBasic;

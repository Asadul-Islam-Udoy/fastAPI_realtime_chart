"use client";

import { useState, useRef, useEffect } from "react";
import { Bell, Menu, X } from "lucide-react";
import Image from "next/image";

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Close dropdown if clicked outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setDropdownOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <nav className="bg-white shadow px-4 py-3 fixed top-0 left-0 right-0 z-50">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        {/* Logo */}
        <div className="text-xl font-bold text-blue-600">ChatApp</div>

        {/* Desktop items */}
        <div className="hidden md:flex items-center gap-4">
          {/* Search input */}
          <input
            type="text"
            placeholder="Search..."
            className="px-3 py-1 text-sm border rounded-full focus:outline-none"
          />

          {/* Notification */}
          <div className="relative">
            <Bell className="w-10 h-7 text-gray-600" />
            <span className="absolute top-0 right-0 bg-red-500 text-white text-xs px-1 rounded-full">
              2
            </span>
          </div>

          {/* Avatar with dropdown */}
          <div className="relative" ref={dropdownRef}>
            <Image
              width={38}
              height={38}
              src="https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png"
              alt="User"
              className="w-10 h-10 rounded-full border-2 border-blue-500 cursor-pointer object-cover"
              onClick={() => setDropdownOpen(!dropdownOpen)}
            />

            {/* Dropdown menu */}
            {dropdownOpen && (
              <div className="absolute right-0 mt-2 w-48 bg-white border rounded shadow z-50">
                <a
                  href="#profile"
                  className="block px-4 py-2 text-sm hover:bg-gray-100"
                >
                  Profile
                </a>
                <a
                  href="#settings"
                  className="block px-4 py-2 text-sm hover:bg-gray-100"
                >
                  Settings
                </a>
                <a
                  href="#logout"
                  className="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100"
                >
                  Logout
                </a>
              </div>
            )}
          </div>
        </div>

        {/* Mobile Menu Button */}
        <button className="md:hidden" onClick={() => setMenuOpen(!menuOpen)}>
          {menuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
        </button>
      </div>

      {/* Mobile Menu Dropdown */}
      {menuOpen && (
        <div className="md:hidden mt-2 space-y-2">
          <input
            type="text"
            placeholder="Search..."
            className="w-full px-3 py-1 text-sm border rounded-full"
          />
          <div className="flex justify-between items-center px-2">
            <div className="relative">
              <Bell className="w-5 h-5 text-gray-600" />
              <span className="absolute top-0 right-0 bg-red-500 text-white text-xs px-1.5 rounded-full">
                2
              </span>
            </div>
            <Image
              width={38}
              height={38}
              src="https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png"
              alt="User"
              className="w-10 h-10 rounded-full border-2 border-blue-500 object-cover"
              onClick={() => setDropdownOpen(!dropdownOpen)}
            />
          </div>
        </div>
      )}
    </nav>
  );
}

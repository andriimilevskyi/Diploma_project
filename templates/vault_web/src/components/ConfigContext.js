// src/ConfigContext.js
import React, { createContext, useState } from 'react';

export const ConfigContext = createContext();

export const ConfigProvider = ({ children }) => {
  const [config, setConfig] = useState({
    discipline: null,
    height: null,
    inseam: null,
    frame: null,
    fork: null,
    // додаватимеш нові етапи сюди
  });

  return (
    <ConfigContext.Provider value={{ config, setConfig }}>
      {children}
    </ConfigContext.Provider>
  );
};

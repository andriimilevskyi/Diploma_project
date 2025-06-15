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

  const updateConfig = (newData) => {
    setConfig(prev => ({ ...prev, ...newData }));
  };

  return (
    <ConfigContext.Provider value={{ config, setConfig, updateConfig }}>
      {children}
    </ConfigContext.Provider>
  );
};

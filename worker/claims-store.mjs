export function d1ClaimsStore(db) {
  return {
    async setJSON(key, value, options = {}) {
      const record = JSON.stringify(value);
      const statement = options.onlyIfNew
        ? db.prepare("INSERT INTO claims (key, record) VALUES (?1, ?2) ON CONFLICT(key) DO NOTHING")
        : db.prepare("INSERT INTO claims (key, record) VALUES (?1, ?2) ON CONFLICT(key) DO UPDATE SET record = excluded.record, updated_at = CURRENT_TIMESTAMP");
      const result = await statement.bind(key, record).run();
      return { modified: result.meta.changes === 1 };
    },
    async get(key) {
      const row = await db.prepare("SELECT record FROM claims WHERE key = ?1").bind(key).first();
      return row ? JSON.parse(row.record) : null;
    },
  };
}

import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { DatabaseSync } from "node:sqlite";
import { d1ClaimsStore } from "../worker/claims-store.mjs";

function sqliteAsD1() {
  const db = new DatabaseSync(":memory:");
  db.exec(readFileSync(new URL("../migrations/0001_claims.sql", import.meta.url), "utf8"));
  return {
    prepare(sql) {
      const statement = db.prepare(sql);
      return {
        bind(...params) {
          return {
            async run() {
              const result = statement.run(...params);
              return { meta: { changes: Number(result.changes) } };
            },
            async first() {
              return statement.get(...params) ?? null;
            },
          };
        },
      };
    },
  };
}

test("only the first conditional write of a key succeeds", async () => {
  const store = d1ClaimsStore(sqliteAsD1());
  assert.deepEqual(await store.setJSON("8453-0xabc", { digest: "a" }, { onlyIfNew: true }), { modified: true });
  assert.deepEqual(await store.setJSON("8453-0xabc", { digest: "b" }, { onlyIfNew: true }), { modified: false });
  assert.deepEqual(await store.get("8453-0xabc"), { digest: "a" });
});

test("an unconditional write replaces the record", async () => {
  const store = d1ClaimsStore(sqliteAsD1());
  await store.setJSON("k", { notified: false }, { onlyIfNew: true });
  assert.deepEqual(await store.setJSON("k", { notified: true }), { modified: true });
  assert.deepEqual(await store.get("k"), { notified: true });
});

test("a missing key reads as null", async () => {
  assert.equal(await d1ClaimsStore(sqliteAsD1()).get("nope"), null);
});

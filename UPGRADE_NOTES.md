# Hayday Store — Upgrade Notes

- Branding updated to **Hayday Store** across application text, docs, examples and metadata.
- Frontends upgraded from Next.js 14 / React 18 to Next.js 16.3.8 / React 19.3.
- TypeScript upgraded to 7.0.2 and ESLint to 9 in frontend/shared packages.
- Backend Django upgraded to 6.1.2 (requires Python 3.12+); `.python-version` uses Python 3.13.
- Graphene-Django upgraded to 3.2.3.
- Removed the old `yarn.lock` because its resolutions were pinned to the old dependency graph; regenerate it with the package manager you choose.
- Package scopes/imports remain `@supastore/*` intentionally to minimize source-level breakage. The user-facing product name is Hayday Store.

Important: Next.js 16 and Django 6.1 are major upgrades. Run dependency installation and the full frontend/backend test/build suite before production deployment. Some third-party packages in this older codebase may need additional compatibility work.

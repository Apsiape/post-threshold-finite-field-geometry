## Zenodo release instructions

These steps are **manual**. This repository can prepare metadata, but it cannot connect accounts, create public releases, or mint the DOI on your behalf.

## Before you start

1. Confirm that `CITATION.cff` and `.zenodo.json` carry the intended public metadata.
2. Confirm the final release tag and version string.
3. Verify that the theorem-status documents match the intended frozen release.

## Manual GitHub + Zenodo workflow

1. Create or confirm the public GitHub repository `Apsiape/post-threshold-finite-field-geometry`.
2. Push the full repository contents to GitHub.
3. Sign in to Zenodo and connect your GitHub account.
4. In Zenodo's GitHub settings, enable archiving for this repository.
5. On GitHub, create a release tag such as `v0.1.0`.
6. Publish the GitHub release.
7. Wait for Zenodo to ingest the release and mint the archive record.
8. In Zenodo, verify the metadata, archive files, and DOI.
9. Copy the DOI badge or DOI URL back into `README.md`.

## Recommended metadata

- **Title:** `post-threshold-finite-field-geometry`
- **Description:** frozen milestone repository for the odd-prime / post-threshold finite-field geometry theorem package
- **Authors:** names, affiliations, and ORCIDs where available
- **Keywords:** finite fields; threshold rigidity; local versus global structure; symbolic verification; reproducible mathematics
- **License:** MIT
- **Version:** release tag, for example `v0.1.0`
- **Related identifiers:** add papers, preprints, or companion repositories if applicable

## After DOI creation

1. Update the README with the DOI badge.
2. Add the DOI to `CITATION.cff` if desired.
3. Optionally add the DOI to a project website or preprint.

## Non-automated steps

The following actions are intentionally manual and cannot be completed from inside this repository:

- connecting GitHub and Zenodo accounts;
- enabling the repository in Zenodo;
- creating and publishing the GitHub release;
- verifying the minted DOI in Zenodo.

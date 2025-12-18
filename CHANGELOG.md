# Changelog

## [0.1.2-rc.0](https://github.com/MapColonies/jobnik-manager-test/compare/v0.1.1-rc.0...v0.1.2-rc.0) (2025-12-18)


### Bug Fixes

* enable include-v-in-tag configuration for release-please ([70d6644](https://github.com/MapColonies/jobnik-manager-test/commit/70d66442a2cbccf8efb21bac0ced0877109787ee))
* remove 'v' prefix from version in release-please manifest ([15a6d72](https://github.com/MapColonies/jobnik-manager-test/commit/15a6d72476f84b8e6f5dee39f0c461c34bfc06ea))
* standardize version format to include 'v' prefix in manifest, changelog, and configuration files ([e4398f1](https://github.com/MapColonies/jobnik-manager-test/commit/e4398f1b719cb61592dbd72031d602eddb2e98ca))
* testing rc increment ([d459c31](https://github.com/MapColonies/jobnik-manager-test/commit/d459c319432010e9efa35b9c275856647244b595))
* update include-v-in-tag configuration for release-please ([ab7837a](https://github.com/MapColonies/jobnik-manager-test/commit/ab7837a0bd802b58983fa5a1ade0f092356ec4e6))
* update release-please configuration for consistency ([a09f7e8](https://github.com/MapColonies/jobnik-manager-test/commit/a09f7e8cd186cbd3a06ea43f2a412aebc75b8df6))

## [v0.1.1-rc.0](https://github.com/MapColonies/jobnik-manager-test/compare/v0.1.0...0.1.1-rc.0) (2025-12-17)


### Bug Fixes

* disable 'include-v-in-tag' in release-please configuration ([47b176a](https://github.com/MapColonies/jobnik-manager-test/commit/47b176a3b0fbe4a6a3730d80d2d168cd1945a6a8))
* switch to release candidate track ([3d919e2](https://github.com/MapColonies/jobnik-manager-test/commit/3d919e23195b7a9e30d08ad7de558cb5c972566e))
* switch to release candidate track ([3be94c2](https://github.com/MapColonies/jobnik-manager-test/commit/3be94c21614f7879832a7da1f6feb59b2f36c555))
* test rc patch bump ([ff1ee83](https://github.com/MapColonies/jobnik-manager-test/commit/ff1ee83ba2ff0dad698d4d5797fe99fa8e0c5505))
* test rc patch bump ([d43731a](https://github.com/MapColonies/jobnik-manager-test/commit/d43731a5950ffbf5442df949afef9e9acea3816b))
* test rc patch bump ([45a51c3](https://github.com/MapColonies/jobnik-manager-test/commit/45a51c3859f5223576394063ff2eb07c3b43e77d))
* test rc patch bump ([e4d1bcc](https://github.com/MapColonies/jobnik-manager-test/commit/e4d1bcc6bcc8a76cd9961be96bf8495f4996148e))
* test rc patch bump ([d39dccc](https://github.com/MapColonies/jobnik-manager-test/commit/d39dccc6a9f6d05057a0978b91e6ee92fdeb9af2))
* test rc patch bump ([5bfaac4](https://github.com/MapColonies/jobnik-manager-test/commit/5bfaac42db6126554c422aaf5bf84740aa5b4c68))
* test rc patch bump ([c7afd88](https://github.com/MapColonies/jobnik-manager-test/commit/c7afd88cd972e9a51c6c2a8c4b0a9295b83f8049))
* test rc patch bump ([874c6d3](https://github.com/MapColonies/jobnik-manager-test/commit/874c6d3ca72fd64d9c028b0fd9f69f7b5c4178c1))

## 0.1.0 (2025-11-16)


### Features

* add comprehensive error handling from OpenAPI spec (MAPCO-7927) ([#89](https://github.com/MapColonies/jobnik-manager/issues/89)) ([225789d](https://github.com/MapColonies/jobnik-manager/commit/225789d6f16a96df96d7a92fe07a055557aad0e2))
* add cron job functionality for task cleanup (MAPCO-8350) ([#94](https://github.com/MapColonies/jobnik-manager/issues/94)) ([8de6cca](https://github.com/MapColonies/jobnik-manager/commit/8de6cca114ca076470663b10be037f95c43df02c))
* add isWaiting flag to stage creation for conditional status handling (MAPCO-7905) ([#40](https://github.com/MapColonies/jobnik-manager/issues/40)) ([e92d6a0](https://github.com/MapColonies/jobnik-manager/commit/e92d6a0efb8bb1127d1f473f2e0e3b05c04af218))
* add metrics for tracking in-progress jobs, stages, and tasks MAPCO-8206 ([#119](https://github.com/MapColonies/jobnik-manager/issues/119)) ([4105597](https://github.com/MapColonies/jobnik-manager/commit/4105597bfa229a7d233fe780a2a060de374466a8))
* add order field to stages for maintaining execution sequence and update related logic (MAPCO-7897) ([#72](https://github.com/MapColonies/jobnik-manager/issues/72)) ([1667e27](https://github.com/MapColonies/jobnik-manager/commit/1667e27a73c0512884cbf5be831069544b059936))
* add Prisma instrumentation for enhanced tracing and update related logic ([#76](https://github.com/MapColonies/jobnik-manager/issues/76)) ([b35aff9](https://github.com/MapColonies/jobnik-manager/commit/b35aff9c55963c770478091c7a8c8f2d97ee63de))
* add startTime and endTime fields to task model (MAPCO-8349) ([#93](https://github.com/MapColonies/jobnik-manager/issues/93)) ([2c17e42](https://github.com/MapColonies/jobnik-manager/commit/2c17e426aec4c9c56730d8985d7c4710a3846014))
* add userMetadata, creationTime, and updateTime to task and stage schemas as mandatory MAPCO-8576 ([#170](https://github.com/MapColonies/jobnik-manager/issues/170)) ([f26268e](https://github.com/MapColonies/jobnik-manager/commit/f26268e68d0196aff546a6c2dc0aa2507f4d2627))
* enhance job, stage and task status update descriptions and validations in OpenAPI spec  MAPCO-8783 ([#171](https://github.com/MapColonies/jobnik-manager/issues/171)) ([bd1c50b](https://github.com/MapColonies/jobnik-manager/commit/bd1c50bebc4a654a7d2b855ac6dea547e397c968))
* enhance tracing attributes in job, stage and task managers  MAPCO-8341 ([#169](https://github.com/MapColonies/jobnik-manager/issues/169)) ([3107027](https://github.com/MapColonies/jobnik-manager/commit/3107027db577bc277225e95d47c6247d6b4fc23a))
* enhance tracing support with traceparent and tracestate fields in jobs, stages, and tasks (MAPCO-8340) ([#78](https://github.com/MapColonies/jobnik-manager/issues/78)) ([b1c78f5](https://github.com/MapColonies/jobnik-manager/commit/b1c78f5ca15a2731d1554d9037241fddbc6190b4))
* implement automatic status propagation across job-stage-task hierarchy MAPCO-8785  MAPCO-8784 ([#153](https://github.com/MapColonies/jobnik-manager/issues/153)) ([7f80168](https://github.com/MapColonies/jobnik-manager/commit/7f8016811d65adeaa75f2491ca5c0a51b55a6fd2))
* implement stage status transition validation and update logic (MAPCO-8803) ([#146](https://github.com/MapColonies/jobnik-manager/issues/146)) ([1201f90](https://github.com/MapColonies/jobnik-manager/commit/1201f90dd0f7d6c6ec3bd738f2520583afcf70d0))
* integrate jobnik manager with config manager & schemas (MAPCO-7924) ([#116](https://github.com/MapColonies/jobnik-manager/issues/116)) ([4c3e716](https://github.com/MapColonies/jobnik-manager/commit/4c3e716a12edf020c6c8f6982d514cd46fee9a42))
* Jobnik Manager: project skeleton & core functions ([#34](https://github.com/MapColonies/jobnik-manager/issues/34)) ([099bc8d](https://github.com/MapColonies/jobnik-manager/commit/099bc8d12c81b18f1d8f76d7658b23bed561e976))


### Bug Fixes

* remove unused previewFeatures from prisma client generator ([2159346](https://github.com/MapColonies/jobnik-manager/commit/2159346088de43d409472bcd018f115245798e43))

# Changelog

## [0.1.1-rc.1](https://github.com/MapColonies/jobnik-manager-test/compare/jobnik-manager-v0.1.0...jobnik-manager-v0.1.1-rc.1) (2026-01-04)


### Features

* add comprehensive error handling from OpenAPI spec (MAPCO-7927) ([#89](https://github.com/MapColonies/jobnik-manager-test/issues/89)) ([225789d](https://github.com/MapColonies/jobnik-manager-test/commit/225789d6f16a96df96d7a92fe07a055557aad0e2))
* add cron job functionality for task cleanup (MAPCO-8350) ([#94](https://github.com/MapColonies/jobnik-manager-test/issues/94)) ([8de6cca](https://github.com/MapColonies/jobnik-manager-test/commit/8de6cca114ca076470663b10be037f95c43df02c))
* add isWaiting flag to stage creation for conditional status handling (MAPCO-7905) ([#40](https://github.com/MapColonies/jobnik-manager-test/issues/40)) ([e92d6a0](https://github.com/MapColonies/jobnik-manager-test/commit/e92d6a0efb8bb1127d1f473f2e0e3b05c04af218))
* add metrics for tracking in-progress jobs, stages, and tasks MAPCO-8206 ([#119](https://github.com/MapColonies/jobnik-manager-test/issues/119)) ([4105597](https://github.com/MapColonies/jobnik-manager-test/commit/4105597bfa229a7d233fe780a2a060de374466a8))
* add order field to stages for maintaining execution sequence and update related logic (MAPCO-7897) ([#72](https://github.com/MapColonies/jobnik-manager-test/issues/72)) ([1667e27](https://github.com/MapColonies/jobnik-manager-test/commit/1667e27a73c0512884cbf5be831069544b059936))
* add Prisma instrumentation for enhanced tracing and update related logic ([#76](https://github.com/MapColonies/jobnik-manager-test/issues/76)) ([b35aff9](https://github.com/MapColonies/jobnik-manager-test/commit/b35aff9c55963c770478091c7a8c8f2d97ee63de))
* add startTime and endTime fields to task model (MAPCO-8349) ([#93](https://github.com/MapColonies/jobnik-manager-test/issues/93)) ([2c17e42](https://github.com/MapColonies/jobnik-manager-test/commit/2c17e426aec4c9c56730d8985d7c4710a3846014))
* add userMetadata, creationTime, and updateTime to task and stage schemas as mandatory MAPCO-8576 ([#170](https://github.com/MapColonies/jobnik-manager-test/issues/170)) ([f26268e](https://github.com/MapColonies/jobnik-manager-test/commit/f26268e68d0196aff546a6c2dc0aa2507f4d2627))
* enhance job, stage and task status update descriptions and validations in OpenAPI spec  MAPCO-8783 ([#171](https://github.com/MapColonies/jobnik-manager-test/issues/171)) ([bd1c50b](https://github.com/MapColonies/jobnik-manager-test/commit/bd1c50bebc4a654a7d2b855ac6dea547e397c968))
* enhance tracing attributes in job, stage and task managers  MAPCO-8341 ([#169](https://github.com/MapColonies/jobnik-manager-test/issues/169)) ([3107027](https://github.com/MapColonies/jobnik-manager-test/commit/3107027db577bc277225e95d47c6247d6b4fc23a))
* enhance tracing support with traceparent and tracestate fields in jobs, stages, and tasks (MAPCO-8340) ([#78](https://github.com/MapColonies/jobnik-manager-test/issues/78)) ([b1c78f5](https://github.com/MapColonies/jobnik-manager-test/commit/b1c78f5ca15a2731d1554d9037241fddbc6190b4))
* implement automatic status propagation across job-stage-task hierarchy MAPCO-8785  MAPCO-8784 ([#153](https://github.com/MapColonies/jobnik-manager-test/issues/153)) ([7f80168](https://github.com/MapColonies/jobnik-manager-test/commit/7f8016811d65adeaa75f2491ca5c0a51b55a6fd2))
* implement stage status transition validation and update logic (MAPCO-8803) ([#146](https://github.com/MapColonies/jobnik-manager-test/issues/146)) ([1201f90](https://github.com/MapColonies/jobnik-manager-test/commit/1201f90dd0f7d6c6ec3bd738f2520583afcf70d0))
* integrate jobnik manager with config manager & schemas (MAPCO-7924) ([#116](https://github.com/MapColonies/jobnik-manager-test/issues/116)) ([4c3e716](https://github.com/MapColonies/jobnik-manager-test/commit/4c3e716a12edf020c6c8f6982d514cd46fee9a42))
* introduce v1 API structure with jobs, stages, and tasks endpoints MAPCO-8959 ([#205](https://github.com/MapColonies/jobnik-manager-test/issues/205)) ([dad0bd3](https://github.com/MapColonies/jobnik-manager-test/commit/dad0bd3b7844346dad9754ed77ec2af42728890a))
* Jobnik Manager: project skeleton & core functions ([#34](https://github.com/MapColonies/jobnik-manager-test/issues/34)) ([099bc8d](https://github.com/MapColonies/jobnik-manager-test/commit/099bc8d12c81b18f1d8f76d7658b23bed561e976))


### Bug Fixes

* 1 ([f0c42a2](https://github.com/MapColonies/jobnik-manager-test/commit/f0c42a26e007ca6dfa09f41dd06e0ae7914d322e))
* 2 ([d5ccfa5](https://github.com/MapColonies/jobnik-manager-test/commit/d5ccfa532346bcdf8b9eb44fc992ce7b36791cd1))
* remove unused previewFeatures from prisma client generator ([2159346](https://github.com/MapColonies/jobnik-manager-test/commit/2159346088de43d409472bcd018f115245798e43))
* restore ([92956e0](https://github.com/MapColonies/jobnik-manager-test/commit/92956e0ef7f7c5387eba3fb93db5b1385a00e012))
* trigger CI ([2490b3d](https://github.com/MapColonies/jobnik-manager-test/commit/2490b3d05980b7de467e2ed4f5cc771d498abb99))
* trigger CI ([a162884](https://github.com/MapColonies/jobnik-manager-test/commit/a162884af9d6f986bf1384e27eadb32fea9bdbf3))
* trigger CI ([96ad1bf](https://github.com/MapColonies/jobnik-manager-test/commit/96ad1bf924a6f24c092e57d245b6367d211d6b9a))
* trigger CI ([3f96e7a](https://github.com/MapColonies/jobnik-manager-test/commit/3f96e7aae979721cff1a181f9d1d17a87e672929))
* trigger CI ([9830c83](https://github.com/MapColonies/jobnik-manager-test/commit/9830c83c62a52ce45fc1e2882ddae37cd4f777d7))
* trigger CI ([6652073](https://github.com/MapColonies/jobnik-manager-test/commit/6652073ca3aa0d6f690d25ac860cc0c2dd9f8ba5))
* trigger rc ([a408c78](https://github.com/MapColonies/jobnik-manager-test/commit/a408c780eec5cbd1fcf478cbba72de7cbc079772))
* trigger rc ([74047f1](https://github.com/MapColonies/jobnik-manager-test/commit/74047f19bf89307831bd0e2f4bcc9a7962efc08d))
* trigger rc ([f71b21d](https://github.com/MapColonies/jobnik-manager-test/commit/f71b21d887f76188eaa8a13c8d37fec2566c80f4))


### Miscellaneous Chores

* enforce correct rc version ([4799343](https://github.com/MapColonies/jobnik-manager-test/commit/47993435ef0d751672de97e4f52aaecaeb6426f5))
* enforce correct rc version ([dd2b2dd](https://github.com/MapColonies/jobnik-manager-test/commit/dd2b2dd031c4e66c5cc3ddfc6711deaa264ae8a7))
* enforce correct rc version ([3e2d60c](https://github.com/MapColonies/jobnik-manager-test/commit/3e2d60ce79d79ce2e09dfea120de3a849c410544))
* enforce correct rc version ([235e037](https://github.com/MapColonies/jobnik-manager-test/commit/235e037f4f3172d919d1ee38309ed279c59a62d5))
* enforce correct rc version ([c4c04d1](https://github.com/MapColonies/jobnik-manager-test/commit/c4c04d10e0f7f966d5042ec4fdaef140d67180de))
* enforce correct rc version ([3f045bd](https://github.com/MapColonies/jobnik-manager-test/commit/3f045bdb92734472e5218e623a24c55e45b2d901))
* enforce correct rc version ([b06cd35](https://github.com/MapColonies/jobnik-manager-test/commit/b06cd3571993f2d8623f94ee1e1c4c354c8e2380))
* enforce correct rc version ([10f383f](https://github.com/MapColonies/jobnik-manager-test/commit/10f383f207b16fb54ed438853da5bda2a3989fe3))
* enforce correct rc version ([ae6468c](https://github.com/MapColonies/jobnik-manager-test/commit/ae6468c54a32b2185defe32333eccce47489bec8))
* enforce correct rc version ([e7031db](https://github.com/MapColonies/jobnik-manager-test/commit/e7031db1453018476514def40bb51e742e80abd7))
* enforce correct rc version ([73fc477](https://github.com/MapColonies/jobnik-manager-test/commit/73fc477670244c9c46868c2d3300b89a5047c443))

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

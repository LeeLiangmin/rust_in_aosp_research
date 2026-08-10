# AOSP 仓库来源分析：外部（third-party）vs AOSP 自研模块

- 仓库总数：3128
- 判定规则：路径约定（external/=第三方导入, prebuilts/=预编译, kernel/+toolchain/=外部基础软件, device/=厂商支持），
  并辅以根目录文件信号校验。

## 1. 总体分类
| 类别 | 仓库数 | 说明 |
|---|---|---|
| third_party | 1519 | 第三方/上游开源项目导入 AOSP（platform/external/*, trusty/external/*） |
| aosp | 782 | AOSP 自研模块（frameworks/system/packages/build/art/bionic…） |
| prebuilt | 362 | 预编译产物仓库（*-prebuilts） |
| vendor_device | 205 | 设备/厂商适配层（device/*, product/*） |
| kernel | 163 | Linux 内核及厂商内核模块（上游 kernel.org / SoC 厂商） |
| toolchain | 70 | 编译工具链（llvm/gcc/rust/jdk，上游外部项目） |
| meta | 27 | manifest/superproject/父项目等元仓库 |

## 2. 外部第三方仓库（1519 个）

| 子类 | 数量 |
|---|---|
| Rust crates（platform/external/rust/crates/*，来自 crates.io） | 470 |
| Google 上游项目（crosvm/minijail/avb 等，仍由 Google 维护但独立上游） | 9 |
| 其他第三方项目 | 1040 |

### 2.1 其他第三方项目（1040 个，节选）

| repo | 说明 |
|---|---|
| external/rust/crates/aarch64-cpu | Bug: 275074143 |
| external/rust/crates/autocfg | Bug: 275074154 |
| platform/external/AFLplusplus | American Fuzzy Lop plus plus (AFL++) Release version: 4.10c  |
| platform/external/ARMComputeLibrary | Bug: 120862079 |
| platform/external/AntennaPod/AntennaPod | AntennaPod This is the official repository of AntennaPod, th |
| platform/external/AntennaPod/AudioPlayer | AntennaPod-AudioPlayer This is the repository for library co |
| platform/external/AntennaPod/afollestad | Material Dialogs Table of Contents (Core) Sample Project Gra |
| platform/external/ComputeLibrary | ⚠ Important From release 22.05: ‘master’ branch has been rep |
| platform/external/FP16 | FP16 Header-only library for conversion to/from half-precisi |
| platform/external/FXdiv | FXdiv Header-only library for division via fixed-point multi |
| platform/external/GhostAWT | Bug: 130345990 |
| platform/external/ImageMagick | - |
| platform/external/Little-CMS | Bug: 436095022 |
| platform/external/MPAndroidChart | :zap: A powerful & easy to use chart library for Android :za |
| platform/external/Mako | - |
| platform/external/Microsoft-GSL | GSL: Guidelines Support Library The Guidelines Support Libra |
| platform/external/Microsoft-unittest-cpp | - |
| platform/external/OpenCL-CLHPP | OpenCLTM API C++ bindings Doxgen documentation for the bindi |
| platform/external/OpenCL-CTS | OpenCL Conformance Test Suite (CTS) This is the OpenCL CTS f |
| platform/external/OpenCL-Headers | OpenCLTM API Headers This repository contains C language hea |
| platform/external/OpenCL-ICD-Loader | OpenCLTM ICD Loader This repo contains the source code and t |
| platform/external/OpenCSD | OpenCSD - An open source CoreSight(tm) Trace Decode library  |
| platform/external/Reactive-Extensions/RxCpp | Bug: 74962500 |
| platform/external/SPIRV-Headers | Bug: 436095022 |
| platform/external/SPIRV-Reflect | Bug: 279043541 |
| platform/external/SPIRV-Tools | Bug: 436095022 |
| platform/external/TestParameterInjector | TestParameterInjector Link to Javadoc. Introduction TestPara |
| platform/external/ThrowTheSwitch-Unity | Bug: 272109169 |
| platform/external/XMP-Toolkit-SDK | Bug: 457231668 |
| platform/external/XNNPACK | XNNPACK XNNPACK is a highly optimized library of floating-po |
| platform/external/aac | - |
| platform/external/abi-compliance-checker | - |
| platform/external/abi-dumper | - |
| platform/external/abseil-cpp | Abseil - C++ Common Libraries The repository contains the Ab |
| platform/external/accessibility-test-framework | Accessibility Test Framework for Android To help people with |
| platform/external/accompanist | Accompanist is a group of libraries that aim to supplement J |
| platform/external/acpica | Bug: 509273825 |
| platform/external/actionbarsherlock | - |
| platform/external/adeb | Bug: 111852163 |
| platform/external/adhd | Bug: 111264136 |
| platform/external/adt-infra | - |
| platform/external/aehd | Bug: 306906844 |
| platform/external/aes | - |
| platform/external/alac | - |
| platform/external/alsa-lib | - |
| platform/external/android-browser-helper | Bug: 509273825 |
| platform/external/android-clat | - |
| platform/external/android-cmake | - |
| platform/external/android-key-attestation | Android Key Attestation Library This library uses the Bouncy |
| platform/external/android-kotlin-demo | Bug: 117121618 |
| platform/external/android-mock | - |
| platform/external/android-nn-driver | Arm NN Android Neural Networks driver This directory contain |
| platform/external/android-studio-gradle-test | - |
| platform/external/android_onboarding | Bug: 299948735 |
| platform/external/androidplot | - |
| platform/external/angle | ANGLE - Almost Native Graphics Layer Engine The goal of ANGL |
| platform/external/animal-sniffer | Bug: 509273825 |
| platform/external/annotation-tools | Bug: 67631744 |
| platform/external/anonymous-counting-tokens | An Implementation of Anonymous Counting Tokens. An anonymous |
| platform/external/ant-glob | - |
| platform/external/antlr | - |
| platform/external/apache-apr | - |
| platform/external/apache-apr-util | - |
| platform/external/apache-commons-bcel | Apache Commons BCEL Apache Commons Bytecode Engineering Libr |
| platform/external/apache-commons-compress | Apache Commons Compress Apache Commons Compress software def |
| platform/external/apache-commons-io | Apache Commons IO The Apache Commons IO library contains uti |
| platform/external/apache-commons-lang | Apache Commons Lang Apache Commons Lang, a package of Java u |
| platform/external/apache-commons-math | - |
| platform/external/apache-harmony | - |
| platform/external/apache-http | - |
| platform/external/apache-log4cxx | - |
| platform/external/apache-qp | Quoted-printable library |
| platform/external/apache-velocity-engine | Title: Apache Velocity Engine Apache Velocity Welcome to Apa |
| platform/external/apache-xml | - |
| platform/external/apple-coreaudiosamples | - |
| platform/external/archive-patcher | Archive Patcher Documentation Copyright 2016 Google Inc. All |
| platform/external/arduino | - |
| platform/external/arduino-ide | - |
| platform/external/argp-standalone | argp-standalone This is a continuation of Niels Möller ‘s wo |
| platform/external/arm-neon-tests | - |
| … 其余 960 个见 origin.csv | |

## 3. AOSP 自研模块（782 个）

| 子树 | 仓库数 | 代表说明 |
|---|---|---|
| platform/packages | 255 | Bug: 335805767 |
| platform/hardware | 154 | Bug: 120215675 |
| platform/system | 126 | Bug: 362954346 |
| platform/frameworks | 69 | Android framework classes and services |
| platform/tools | 67 | Android Automotive Developer Tools AADevT contains |
| platform/test | 28 | Bug: 140192942 |
| platform/build | 12 | Android Make Build System This is the Makefile-bas |
| trusty/app | 11 | Bug: 371226688 |
| trusty/device | 8 | Bug: 390682260 |
| platform/bootable | 5 | bootloader reference code |
| platform/developers | 4 | - |
| trusty/lk | 3 | LK The LK embedded kernel. An SMP-aware kernel des |
| trusty/host | 2 | Documentation for this project is currently mainta |
| assets/android-studio-ux-assets | 1 | Bug: 32992167 |
| platform/abi | 1 | - |
| platform/apisurface | 1 | Bug: 236926434 |
| platform/art | 1 | - |
| platform/bbuildbot_config | 1 | This repository exists to configure cbuildbot base |
| platform/bionic | 1 | bionic maintainer overview bionic is Android's C l |
| platform/brillo | 1 | - |
| platform/compatibility | 1 | See instructions in cdd_gen.sh |
| platform/cts | 1 | Compatibility Test Suite |
| platform/dalvik | 1 | Dalvik virtual machine and core libraries |
| platform/dalvik-snapshot | 1 | - |
| platform/dalvik2 | 1 | - |
| platform/development | 1 | Platform engineering tools, sample code |
| platform/docs | 1 | Source files for the source.android.com site. |
| platform/gdk | 1 | - |
| platform/libcore | 1 | Android Core Library Existing open bugs File a new |
| platform/libcore-snapshot | 1 | - |
| platform/libcore2 | 1 | - |
| platform/libnativehelper | 1 | libnativehelper libnativehelper is a collection of |
| platform/media | 1 | Bug: 177363648 |
| platform/motodev | 1 | - |
| platform/ndk | 1 | Android Native Development Kit (NDK) The latest ve |
| platform/pdk | 1 | - |
| platform/platform_testing | 1 | - |
| platform/prebuilt | 1 | binaries to support linux and osx builds |
| platform/sdk | 1 | Development Tools for the SDK |
| platform/smaratorg | 1 | Bug: 117210240 |
| tools/aospstats | 1 | A project to collect and display stats about AOSP. |
| tools/fetch_artifact | 1 | Fetch Artifact Fetch artifact is a tool for downlo |
| tools/platform-compat | 1 | Platform compat tools Tools for Android App Compat |
| tools/plugin-testing | 1 | Bug: 77581061

Owner: samccone@ |
| tools/presubmit-automerger | 1 | Bug: 151974301 |
| tools/repo | 1 | repo Repo is a tool built on top of Git. Repo help |
| trusty | 1 | For ACL only |
| trusty/interfaces | 1 | Bug: 254766677 |
| trusty/lib | 1 | - |
| trusty/user | 1 | Bug: 361072469 |
| trusty/vendor | 1 | - |

## 4. 设备/厂商适配（205 个）

- device/google: 108
- device/generic: 24
- device/linaro: 9
- device/htc: 8
- device/samsung: 8
- device/asus: 7
- device/lge: 6
- device/moto: 5
- device/ti: 4
- platform/vendor: 3
- device/amlogic: 2
- device/huawei: 2
- device/intel: 2
- product/google: 2
- device/aaeon: 1
- device/casio: 1
- device/common: 1
- device/freescale: 1
- device/google_car: 1
- device/imagination: 1
- device/marvell: 1
- device/mediatek: 1
- device/pifoundation: 1
- device/qcom: 1
- device/rockchip: 1
- device/sample: 1
- device/samsung_slsi: 1
- device/sony: 1
- tee/optee: 1

## 5. 与 Rust 信号交叉
- 外部仓库中具 Rust 强信号的：450 个

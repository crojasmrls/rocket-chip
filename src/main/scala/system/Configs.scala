// See LICENSE.SiFive for license details.
// See LICENSE.Berkeley for license details.

package freechips.rocketchip.system

import Chisel._
import freechips.rocketchip.config.Config
import freechips.rocketchip.coreplex._
import freechips.rocketchip.devices.debug.{IncludeJtagDTM, JtagDTMKey}
import freechips.rocketchip.diplomacy._

class WithJtagDTMSystem extends freechips.rocketchip.coreplex.WithJtagDTM

class BaseConfig extends Config(new BaseCoreplexConfig().alter((site,here,up) => {
  // DTS descriptive parameters
  case DTSModel => "freechips,rocketchip-unknown"
  case DTSCompat => Nil
  case DTSTimebase => BigInt(1000000) // 1 MHz
  // External port parameters
  case NExtTopInterrupts => 2
  case ExtMem => MasterPortParams(
                      base = x"8000_0000",
                      size = x"1000_0000",
                      beatBytes = site(MemoryBusKey).beatBytes,
                      idBits = 4)
  case ExtBus => MasterPortParams(
                      base = x"6000_0000",
                      size = x"2000_0000",
                      beatBytes = site(MemoryBusKey).beatBytes,
                      idBits = 4)
  case ExtIn  => SlavePortParams(beatBytes = 8, idBits = 8, sourceBits = 4)
}))

class DefaultConfig extends Config(new WithNBigCores(1) ++ new BaseConfig)

class DefaultBufferlessConfig extends Config(
  new WithBufferlessBroadcastHub ++ new WithNBigCores(1) ++ new BaseConfig)

class DefaultSmallConfig extends Config(new WithNSmallCores(1) ++ new BaseConfig)
class DefaultRV32Config extends Config(new WithRV32 ++ new DefaultConfig)

class DualBankConfig extends Config(
  new WithNBanksPerMemChannel(2) ++ new BaseConfig)

class DualChannelConfig extends Config(new WithNMemoryChannels(2) ++ new BaseConfig)

class DualChannelDualBankConfig extends Config(
  new WithNMemoryChannels(2) ++
  new WithNBanksPerMemChannel(2) ++ new BaseConfig)

class RoccExampleConfig extends Config(new WithRoccExample ++ new DefaultConfig)

class Edge128BitConfig extends Config(
  new WithEdgeDataBits(128) ++ new BaseConfig)
class Edge32BitConfig extends Config(
  new WithEdgeDataBits(32) ++ new BaseConfig)

class SingleChannelBenchmarkConfig extends Config(new DefaultConfig)
class DualChannelBenchmarkConfig extends Config(new WithNMemoryChannels(2) ++ new SingleChannelBenchmarkConfig)
class QuadChannelBenchmarkConfig extends Config(new WithNMemoryChannels(4) ++ new SingleChannelBenchmarkConfig)
class OctoChannelBenchmarkConfig extends Config(new WithNMemoryChannels(8) ++ new SingleChannelBenchmarkConfig)

class EightChannelConfig extends Config(new WithNMemoryChannels(8) ++ new BaseConfig)

class DualCoreConfig extends Config(
  new WithNBigCores(2) ++ new BaseConfig)

class TinyConfig extends Config(
  new WithNMemoryChannels(0) ++
  new WithIncoherentTiles ++
  new With1TinyCore ++
  new BaseConfig)

class BaseFPGAConfig extends Config(new BaseConfig)

class DefaultFPGAConfig extends Config(new WithNSmallCores(1) ++ new BaseFPGAConfig)
class DefaultFPGASmallConfig extends Config(new DefaultFPGAConfig)


//MA Configs Coherence Protocols

class MESI2Config extends Config(
  new WithNBigCores(2) ++ 
  new BaseConfig)

class MSI2Config extends Config(
  new WithNBigCores(2) ++ 
  new WithMSICoherence ++
  new BaseConfig)

class MI2Config extends Config(
  new WithNBigCores(2) ++ 
  new WithMICoherence ++
  new BaseConfig)



class MESI4Config extends Config(
  new WithNBigCores(4) ++ 
  new BaseConfig)

class MSI4Config extends Config(
  new WithNBigCores(4) ++ 
  new WithMSICoherence ++
  new BaseConfig)

class MI4Config extends Config(
  new WithNBigCores(4) ++ 
  new WithMICoherence ++
  new BaseConfig)



class MESI6Config extends Config(
  new WithNBigCores(6) ++ 
  new BaseConfig)

class MSI6Config extends Config(
  new WithNBigCores(6) ++ 
  new WithMSICoherence ++
  new BaseConfig)

class MI6Config extends Config(
  new WithNBigCores(6) ++ 
  new WithMICoherence ++
  new BaseConfig)



class MESI8Config extends Config(
  new WithNBigCores(8) ++ 
  new BaseConfig)

class MSI8Config extends Config(
  new WithNBigCores(8) ++ 
  new WithMSICoherence ++
  new BaseConfig)

class MI8Config extends Config(
  new WithNBigCores(8) ++ 
  new WithMICoherence ++
  new BaseConfig)
import ApplicabilityProofs

/-!
The true member of the supplied applicability family follows from the declared
sensor/extraction coupling. This is a model-side witness, not a controller input:
the selection procedure receives neither these flags nor the witness. The local
coupling law and calibration remain premises of the represented apparatus.
-/

namespace AcquiredApplicability

def actualUse (cfg : Config) : Candidate :=
  if cfg.blocked then .blocked
  else if cfg.sigma then .complement else .identity

theorem actualUse_mem_family (cfg : Config) : actualUse cfg ∈ family := by
  unfold actualUse
  split
  · exact .tail _ (.tail _ (.head _))
  · split
    · exact .tail _ (.head _)
    · exact .head _

/-- Sensor and productive readiness differentiate through this declared
coupling. The readiness transformation tau does not by itself determine which
retained sensory reading is productive. -/
theorem actualUse_calibrated (cfg : Config) (raw : Bool) :
    arrival (actualUse cfg) (raw ^^ cfg.tau ^^ cfg.sigma) =
      ((raw ^^ cfg.tau) && !cfg.blocked) := by
  cases cfg with
  | mk environment tau sigma brokenReset blocked receiptMode clamp deny =>
    cases blocked <;> cases sigma <;> cases tau <;> cases raw <;> rfl

/-- The actual source operation realizes the calibrated relation when its
packet is available. This operation follows its separately charged preparation.
Its guard must not be dropped: without source it records no new arrival. -/
theorem extraction_realizes_actualUse (cfg : Config) (b : Body)
    (hs : 10 ≤ b.physical.source) :
    (extracted cfg b).actualArrival = arrival (actualUse cfg)
      (cfg.environment.output b.physical.phase ^^ cfg.tau ^^ cfg.sigma) := by
  unfold extracted
  rw [if_neg (Nat.not_lt_of_ge hs)]
  exact (actualUse_calibrated cfg (cfg.environment.output b.physical.phase)).symm

/-- A faithful physical receipt retains the true member when it was still
admitted. Sensor and receipt here refer to the same unchanged encounter phase;
the two explicit equalities expose that calibration and temporal premise. -/
theorem faithful_physical_update_retains (cfg : Config) (cs : List Candidate)
    (raw sensor receipt : Bool) (hc : actualUse cfg ∈ cs)
    (hs : sensor = (raw ^^ cfg.tau ^^ cfg.sigma))
    (hr : receipt = ((raw ^^ cfg.tau) && !cfg.blocked)) :
    actualUse cfg ∈ update cs sensor receipt := by
  rw [hs, hr]
  exact faithful_candidate_retained _ _ _ _ hc (actualUse_calibrated cfg raw)

theorem first_faithful_physical_update_retains (cfg : Config)
    (raw sensor receipt : Bool)
    (hs : sensor = (raw ^^ cfg.tau ^^ cfg.sigma))
    (hr : receipt = ((raw ^^ cfg.tau) && !cfg.blocked)) :
    actualUse cfg ∈ update family sensor receipt :=
  faithful_physical_update_retains cfg family raw sensor receipt
    (actualUse_mem_family cfg) hs hr

#print axioms actualUse
#print axioms actualUse_mem_family
#print axioms actualUse_calibrated
#print axioms extraction_realizes_actualUse
#print axioms faithful_physical_update_retains
#print axioms first_faithful_physical_update_retains

end AcquiredApplicability

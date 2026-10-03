import contract from '../../production/contracts/carrier-construction.json';
import type { CatalogueId, PartKind, Vec3 } from './types';

/** Shared authored geometry/mass contract. No value here upgrades its qualification. */
export const constructionContract = contract;
export const catalogueRevision = contract.revision;
export function cataloguePart(id: CatalogueId) {
  const material = contract.parts.find(part => part.id === id);
  if (!material) throw new Error(`Construction contract ${contract.revision} has no material ${id}`);
  return { ...material, dimensionsM_YUp: [...material.dimensionsM_YUp] as Vec3 };
}
export function defaultCatalogueId(kind: PartKind): CatalogueId {
  return kind === 'temp_brace' ? 'temporary_brace' : kind === 'temp_service' ? 'service' : kind;
}
